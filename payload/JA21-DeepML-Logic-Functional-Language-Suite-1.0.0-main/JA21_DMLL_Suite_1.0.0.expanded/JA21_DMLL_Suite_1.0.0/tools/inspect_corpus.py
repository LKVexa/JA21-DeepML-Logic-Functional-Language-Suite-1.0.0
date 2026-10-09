#!/usr/bin/env python3
"""Offline inspector for the JA21 DMLL technical corpus."""
from __future__ import annotations
import argparse, gzip, json, sys
from pathlib import Path

def open_text(path: Path):
    return gzip.open(path, "rt", encoding="utf-8") if path.suffix == ".gz" else path.open("r", encoding="utf-8")

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--topic")
    ap.add_argument("--tier")
    ap.add_argument("--class-name", dest="class_name")
    ap.add_argument("--id")
    ap.add_argument("--limit", type=int, default=20)
    args=ap.parse_args()
    shown=0
    with open_text(args.corpus) as f:
        for line_no,line in enumerate(f,1):
            try: r=json.loads(line)
            except json.JSONDecodeError as e:
                print(f"invalid JSON on line {line_no}: {e}",file=sys.stderr); return 2
            if args.topic and r.get("topic") != args.topic: continue
            if args.tier and str(r.get("tier_name")) != args.tier and str(r.get("tier")) != args.tier: continue
            if args.class_name and r.get("example_class") != args.class_name: continue
            if args.id and r.get("id") != args.id: continue
            print(json.dumps({k:r.get(k) for k in ("id","topic","tier_name","example_class","expected_stage","diagnostic_id")},ensure_ascii=False))
            shown += 1
            if shown >= args.limit: break
    return 0
if __name__=="__main__": raise SystemExit(main())
