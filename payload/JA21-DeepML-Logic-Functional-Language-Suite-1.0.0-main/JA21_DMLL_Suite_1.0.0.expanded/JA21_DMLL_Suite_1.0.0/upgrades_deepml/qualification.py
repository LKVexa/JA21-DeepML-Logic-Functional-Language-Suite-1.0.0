"""Offline evidence qualification for six supplied DeepML corpus profiles.

This module inspects metadata and hashes only. It never executes source programs.
"""
from __future__ import annotations
import hashlib
import re

SCHEMA_VERSION = "deepml-audit-0.1"


def source_of(record):
    source = record.get("source")
    if isinstance(source, str):
        return source
    if isinstance(source, dict):
        return source.get("program", "")
    return ""


def identity_of(record):
    identity = record.get("identity", {})
    return (identity.get("id") or record.get("id") or record.get("record_id"),
            identity.get("language") or record.get("profile_id") or record.get("language"))


def source_hash_of(record):
    source = record.get("source", {})
    if isinstance(source, dict):
        supplied = source.get("source_hash")
    else:
        supplied = record.get("source_hash") or record.get("hashes", {}).get("source")
    if not supplied:
        supplied = record.get("ast", {}).get("origin_hash")
    return str(supplied or "").removeprefix("sha256:")


def expected_of(record):
    validation = record.get("validation") or record.get("validation_result") or {}
    return validation.get("expected") or validation.get("expected_status") or "unspecified"


def device_warnings(record):
    source = source_of(record)
    match = re.search(r"^target\s+([A-Za-z_][A-Za-z_0-9]*)\s*$", source, re.MULTILINE)
    if not match:
        return []
    target = match.group(1)
    ast = record.get("ast", {})
    semantic = record.get("semantic_interpretation", {})
    r12 = record.get("compiler_representation", {}).get("r12", {})
    runtime = record.get("runtime_representation", {})
    fields = [
        ("ast.effect_set", ast.get("effect_set", [])),
        ("ast.capability_requirements", ast.get("capability_requirements", [])),
        ("semantic_interpretation.effects", semantic.get("effects", [])),
        ("semantic_interpretation.capabilities", semantic.get("capabilities", [])),
        ("compiler_representation.r12.effects", r12.get("effects", [])),
        ("compiler_representation.r12.capabilities", r12.get("capabilities", [])),
        ("runtime_representation.effects_observed", runtime.get("effects_observed", [])),
        ("runtime_representation.capabilities_consumed", runtime.get("capabilities_consumed", [])),
    ]
    warnings = []
    for path, values in fields:
        devices = sorted({v.split(".", 1)[1] for v in values
                          if isinstance(v, str) and v.startswith("device.")})
        if devices and target not in devices:
            warnings.append({"code": "DEVICE_TARGET_METADATA_MISMATCH", "path": path,
                             "source_target": target, "reported_devices": devices})
    return warnings


def qualify(record, profile):
    program = source_of(record)
    observed_hash = hashlib.sha256(program.encode("utf-8")).hexdigest()
    supplied_hash = source_hash_of(record)
    warnings = device_warnings(record)
    if supplied_hash != observed_hash:
        warnings.append({"code": "SOURCE_HASH_MISMATCH", "path": "source",
                         "expected_hash": supplied_hash, "computed_hash": observed_hash})
    audit = {
        "schema_version": SCHEMA_VERSION,
        "profile": profile,
        "execution_state": "modeled_not_executed",
        "expected_outcome": expected_of(record),
        "observed_result": None,
        "native_execution_eligible": False,
        "source_sha256": observed_hash,
        "source_hash_verified": supplied_hash == observed_hash,
        "qualification": "quarantined_metadata_conflict" if warnings else "modeled_expectation_only",
        "warnings": warnings,
        "authority": "Structural/hash audit only; no parse, type, proof, device or runtime execution evidence.",
    }
    return audit


def audit_schema(profile):
    return {
        "type": "object",
        "required": ["schema_version", "profile", "execution_state", "expected_outcome",
                     "observed_result", "native_execution_eligible", "source_sha256",
                     "source_hash_verified", "qualification", "warnings", "authority"],
        "additionalProperties": False,
        "properties": {
            "schema_version": {"const": SCHEMA_VERSION},
            "profile": {"const": profile},
            "execution_state": {"const": "modeled_not_executed"},
            "expected_outcome": {"type": "string"},
            "observed_result": {"type": "null"},
            "native_execution_eligible": {"const": False},
            "source_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
            "source_hash_verified": {"type": "boolean"},
            "qualification": {"enum": ["modeled_expectation_only", "quarantined_metadata_conflict"]},
            "warnings": {"type": "array", "items": {"type": "object", "required": ["code", "path"]}},
            "authority": {"type": "string", "minLength": 1},
        },
    }
