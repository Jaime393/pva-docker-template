# LECTURA — pva-docker-template

Repo: `Jaime393/pva-docker-template`, rama `main`.
Leído en vivo 2026-11-09 ~07:07 -05. Un solo commit, 2026-09-10.

## Lo que el repo dice de sí mismo

El README (535 B) lo presenta así, textual:

> "# pva-docker-template V202 — ρ(x)>0
>
> Plantilla reproducibilidad universal — cualquier paper se ejecuta con un
> solo comando."

Y da tres formas de uso: `make repro`, `docker build -t pva-paper .` +
`docker run --rm pva-paper`, o `docker-compose up`.

Afirma que incluye:

- "Dockerfile base python:3.11-slim + make" — SÉ, el Dockerfile dice
  `FROM python:3.11-slim` e instala `make`.
- "docker-compose.yml" — SÉ, existe (128 B).
- "Makefile con objetivos: repro, dev, test, lint, reproduce" — SÉ, los 5
  existen en el Makefile (285 B).
- "data/GRACE_TN14_REAL_TEMPLATE.csv C20 -0.0004846999 DOI
  10.1029/2019GL085488 Ktau 0.3644 r=-0.868" — SÉ que el CSV existe y que
  esos números aparecen como texto en el README; su verdad se trata en
  CONTENIDO.md.
- "scripts/verify_data.py" y "scripts/repro.py" — SÉ, ambos existen.

Cierra con: "PVA score esperado: 1.0" — "esperado", no medido. Ningún
archivo del repo calcula un PVA score (ver INVENTARIO.md).

## Lo que dicen los datos

`data/README.md` (86 B), textual:

> "# data — GRACE TN14 C20 -0.0004846999 221 filas IERS C04 + DOI
> 10.1029/2019GL085488"

Esa línea afirma 221 filas y fuente IERS C04. El CSV que acompaña tiene
7 filas de datos y columna `source` con valor `GRACE_TN14` en las 7.
La discrepancia se documenta en CONTENIDO.md; aquí solo se registra
lo que cada archivo dice.

## Lo que dicen los scripts

- `scripts/repro.py` imprime "=== PVA-DOCKER-TEMPLATE REPRO V202 ===",
  el número de filas, el último C20, y la línea literal
  "Ktau ejemplo 0.3644 r=-0.868 sigma_ref 1.35e-10". Escribe
  `fig_C20.png` con bytes `dummy` y anuncia "Repro OK — figura
  fig_C20.png generada (dummy)".
- `scripts/verify_data.py` imprime "Verificando ..." y, si el CSV existe
  y tiene ≥3 filas, "OK integridad datos". El umbral (≥3) está por debajo
  de las 7 filas reales.

## Lo que dice el CI

`.github/workflows/pva.yml` ("PVA docker repro", on push y pull_request):
hace checkout, `docker build -t pva-paper .`, `docker run --rm pva-paper`,
y `python scripts/verify_data.py || echo "skip"` — el fallo de la
verificación no tumba el trabajo (el `|| echo "skip"` lo traga).

No se ejecutó nada: esta minería es solo lectura. NO SÉ si el build de
docker funciona, si `make repro` corre, ni si el CI llegó a pasar alguna
vez (no se consultaron los runs).
