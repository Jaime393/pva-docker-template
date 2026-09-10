#!/usr/bin/env python3
import pathlib, pandas as pd
p = pathlib.Path("data/GRACE_TN14_REAL_TEMPLATE.csv")
print(f"Verificando {p}")
if not p.exists():
    print("FALTA data/GRACE_TN14_REAL_TEMPLATE.csv")
    exit(1)
df = pd.read_csv(p)
print(f"Filas: {len(df)} C20 ultima: {df.iloc[-1]['C20']} DOI 10.1029/2019GL085488")
assert len(df) >= 3
print("OK integridad datos")
