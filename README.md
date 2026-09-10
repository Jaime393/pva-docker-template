# pva-docker-template V202 — ρ(x)>0

Plantilla reproducibilidad universal — cualquier paper se ejecuta con un solo comando.

```bash
make repro
# o
docker build -t pva-paper .
docker run --rm pva-paper
# o
docker-compose up
```

Incluye:
- Dockerfile base python:3.11-slim + make
- docker-compose.yml
- Makefile con objetivos: repro, dev, test, lint, reproduce
- data/GRACE_TN14_REAL_TEMPLATE.csv C20 -0.0004846999 DOI 10.1029/2019GL085488 Ktau 0.3644 r=-0.868
- scripts/verify_data.py
- scripts/repro.py

PVA score esperado: 1.0
