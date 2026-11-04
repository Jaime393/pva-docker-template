#!/usr/bin/env python3
"""Check CSV structure and report descriptive values, not provenance or physics."""
import argparse
import csv
from datetime import date
import hashlib
import io
import json
import math
from pathlib import Path

DEFAULT_DATA = Path(__file__).resolve().parents[1] / "data/GRACE_TN14_REAL_TEMPLATE.csv"
MAX_BYTES = 2 * 1024 * 1024


def inspect_csv(path=DEFAULT_DATA):
    path = Path(path)
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError("bounded regular CSV required")
    raw = path.read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    if not reader.fieldnames or not {"date", "C20", "source"} <= set(reader.fieldnames):
        raise ValueError("date, C20 and source columns required")
    rows = list(reader)
    if not rows or len(rows) > 10000:
        raise ValueError("CSV requires 1..10000 records")
    dates, values, claims = [], [], set()
    for row in rows:
        dates.append(date.fromisoformat(row["date"]))
        value = float(row["C20"])
        if not math.isfinite(value) or not row["source"]:
            raise ValueError("finite C20 and nonempty source label required")
        values.append(value)
        claims.add(row["source"])
    if len(set(dates)) != len(dates):
        raise ValueError("duplicate observation dates")
    return {"schema": "pva.csv-summary/v1", "data_sha256": hashlib.sha256(raw).hexdigest(),
            "rows": len(rows), "first_date": min(dates).isoformat(), "last_date": max(dates).isoformat(),
            "C20": {"min": min(values), "max": max(values), "mean": sum(values) / len(values)},
            "source_labels_reported": sorted(claims), "provenance_verified": False,
            "scientific_claims_validated": False, "network_used": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args(argv)
    try:
        result = inspect_csv(args.data)
    except (OSError, ValueError, TypeError, KeyError):
        parser.exit(2, "Blocked: invalid, missing or oversized CSV.\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
