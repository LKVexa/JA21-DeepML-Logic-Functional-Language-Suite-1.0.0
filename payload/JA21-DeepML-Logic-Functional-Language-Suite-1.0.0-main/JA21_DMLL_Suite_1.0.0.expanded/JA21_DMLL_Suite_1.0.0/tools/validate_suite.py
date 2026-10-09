#!/usr/bin/env python3
"""Structural validator for JA21 DeepML Logic/Functional Suite 1.0.0."""
from __future__ import annotations
import csv, gzip, hashlib, json, sys
from pathlib import Path

def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main() -> int:
    root=Path(__file__).resolve().parents[1]
    errors=[]
    corpus=root/"corpus/technical/deepml_logic_functional_technical_corpus_10000.jsonl.gz"
    records=[]
    with gzip.open(corpus,"rt",encoding="utf-8") as f:
        for i,line in enumerate(f,1):
            try:r=json.loads(line)
            except Exception as e:
                errors.append(f"corpus line {i}: {e}");continue
            records.append(r)
            expected=str(r.get("source_hash","")).split(":",1)[-1]
            if sha_text(r.get("source","")) != expected:
                errors.append(f"{r.get('id')}: source hash mismatch")
    if len(records)!=10000:errors.append(f"record count {len(records)} != 10000")
    ids=[r.get("id") for r in records]
    if len(set(ids))!=len(ids):errors.append("duplicate record IDs")
    if [r.get("sequence") for r in records] != list(range(1,10001)):errors.append("sequence is not 1..10000")
    scripts=sorted((root/"scripts").rglob("*.deepml"))
    if len(scripts)!=1000:errors.append(f"script count {len(scripts)} != 1000")
    with (root/"catalogs/SCRIPT_CATALOG.csv").open(encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=1000:errors.append(f"catalog count {len(rows)} != 1000")
    rowmap={r["script_id"]:r for r in rows}
    for p in scripts:
        sid=p.stem
        text=p.read_text(encoding="utf-8")
        if sid not in rowmap:errors.append(f"{sid}: missing catalog row");continue
        if not text.startswith("deepml logic 0.3"):errors.append(f"{sid}: bad header")
        if "policy pure_by_default" not in text:errors.append(f"{sid}: missing purity policy")
        if "policy no_network" not in text:errors.append(f"{sid}: missing no-network policy")
        if text.count("{") != text.count("}"):errors.append(f"{sid}: unbalanced braces")
        if sha_text(text.rstrip()+"\n") != rowmap[sid]["source_hash"].split(":",1)[-1] and sha_text(text.rstrip()) != rowmap[sid]["source_hash"].split(":",1)[-1]:
            errors.append(f"{sid}: script hash mismatch")
    topics={r["topic"] for r in records}
    tiers={str(r["tier_name"]) for r in records}
    classes={r["example_class"] for r in records}
    if len(topics)!=46:errors.append(f"topic coverage {len(topics)} != 46")
    if len(tiers)!=6:errors.append(f"tier coverage {len(tiers)} != 6")
    if classes!={"positive","negative","certification"}:errors.append(f"class coverage {classes}")
    if errors:
        print("FAIL")
        for e in errors[:100]:print("-",e)
        if len(errors)>100:print(f"... {len(errors)-100} more")
        return 1
    print("PASS")
    print(f"records={len(records)} scripts={len(scripts)} topics={len(topics)} tiers={len(tiers)}")
    return 0
if __name__=="__main__":raise SystemExit(main())
