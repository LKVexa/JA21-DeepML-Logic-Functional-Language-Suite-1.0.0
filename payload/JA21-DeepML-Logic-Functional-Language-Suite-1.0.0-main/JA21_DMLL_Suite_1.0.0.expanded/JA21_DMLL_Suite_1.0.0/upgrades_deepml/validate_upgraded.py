"""Validate an upgraded DeepML suite without executing its source language.

Requires jsonschema. Run from any directory: python validate_upgraded.py.
Schemas are local and remote references are refused before constructing a validator.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import platform
for _ancestor in Path(__file__).resolve().parents:
    _vendor = _ancestor / "tools" / "vendor"
    if _vendor.is_dir() and sys.platform == "win32" and sys.version_info[:2] == (3, 12) and platform.machine().lower() in ("amd64", "x86_64") and sys.implementation.name == "cpython":
        sys.path.insert(0, str(_vendor))
        break

from qualification import qualify, identity_of, source_of


def refuse_external_references(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"$ref", "$dynamicRef"} and not str(child).startswith("#"):
                raise ValueError(f"External schema reference refused: {child}")
            refuse_external_references(child)
    elif isinstance(value, list):
        for child in value:
            refuse_external_references(child)


def load_validator(schema):
    refuse_external_references(schema)
    try:
        from jsonschema import Draft202012Validator
    except ImportError as error:
        raise RuntimeError("Install the jsonschema dependency before validation; no fallback schema claim is made.") from error
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_record(record, profile, validator):
    errors = [f"schema:{'/'.join(str(x) for x in e.absolute_path)}:{e.message}"
              for e in validator.iter_errors(record)]
    rid, observed_profile = identity_of(record)
    if observed_profile != profile:
        errors.append(f"profile mismatch: {observed_profile!r} != {profile!r}")
    sequence = record.get("identity", {}).get("sequence", record.get("sequence"))
    if not isinstance(sequence, int) or not isinstance(rid, str) or rid.rsplit("-", 1)[-1] != f"{sequence:05d}":
        errors.append("record identity/sequence mismatch")
    program = source_of(record)
    expected_header = "ja source 0.3" if profile == "deepml.kernel" else f"deepml {profile.split('.')[-1]} 0.3"
    if not program.startswith(expected_header + "\n"):
        errors.append("source envelope mismatch")
    if not any(line.strip() == "policy no_network" for line in program.splitlines()):
        errors.append("missing standalone no_network policy")
    expected_audit = qualify(record, profile)
    if record.get("_deepml_audit") != expected_audit:
        errors.append("audit extension does not match independent hash/device qualification")
    if not expected_audit["source_hash_verified"]:
        errors.append("supplied source hash disagrees with exact UTF-8 program")
    return errors


def run(root):
    upgrade = root / "upgrades_deepml"
    config = json.loads((upgrade / "profile.json").read_text(encoding="utf-8"))
    schema_path = (root / config["schema_path"]).resolve()
    if not schema_path.is_relative_to(root.resolve()):
        raise ValueError("Configured schema path escapes suite root")
    if Path(config["master"]).name != config["master"]:
        raise ValueError("Configured master must be a filename in corpus/technical")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = load_validator(schema)
    profile = config["profile"]
    reports = []
    master_ids = {}
    shard_ids = {}
    failures = []
    for path in sorted((root / "corpus" / "technical").glob("*.jsonl.gz")):
        seen = set()
        report = {"path": path.relative_to(root).as_posix(), "records": 0,
                  "quarantined_records": 0, "schema_hash_policy_errors": 0}
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, 1):
                try:
                    record = json.loads(line)
                    rid, _ = identity_of(record)
                    errors = validate_record(record, profile, validator)
                    if rid in seen:
                        errors.append("duplicate record identity within dataset")
                    seen.add(rid)
                    report["records"] += 1
                    if record["_deepml_audit"]["qualification"] == "quarantined_metadata_conflict":
                        report["quarantined_records"] += 1
                    digest = hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()
                    if path.name == config["master"]:
                        master_ids[rid] = digest
                    else:
                        if rid in shard_ids:
                            errors.append("record repeats across shards")
                        shard_ids[rid] = digest
                    if errors:
                        report["schema_hash_policy_errors"] += 1
                        if len(failures) < 50:
                            failures.append({"path": report["path"], "line": line_number, "id": rid, "errors": errors[:5]})
                except (ValueError, KeyError, TypeError) as error:
                    report["schema_hash_policy_errors"] += 1
                    if len(failures) < 50:
                        failures.append({"path": report["path"], "line": line_number, "errors": [str(error)]})
        reports.append(report)
    if len(master_ids) != 10000:
        failures.append({"errors": [f"master identity count {len(master_ids)} != 10000"]})
    if shard_ids and master_ids != shard_ids:
        mismatched = [rid for rid in master_ids if shard_ids.get(rid) != master_ids[rid]]
        failures.append({"errors": ["master/shard record content differs"], "example_ids": mismatched[:10]})
    return {"status": "PASS" if not failures else "FAIL", "authority": "schema, hashes, standalone policy, metadata qualification and master/shard equality only",
            "native_language_conformance": "not_tested", "profile": profile,
            "unique_master_records": len(master_ids), "datasets": reports, "failures": failures}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        result = run(args.root.resolve())
    except (RuntimeError, ValueError, OSError) as error:
        print(json.dumps({"status": "FAIL", "error": str(error)}, indent=2))
        return 1
    if args.report:
        args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
