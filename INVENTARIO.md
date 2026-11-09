# INVENTARIO — pva-docker-template

Minería ola 4, tanda 1. Repo: `Jaime393/pva-docker-template`, rama `main`.
Leído en vivo 2026-11-09 ~07:07 -05 (get_file_contents por archivo).
Total: **11 archivos, 2.836 B**. Sin subdirectorios con contenido salvo `data/`,
`scripts/` y `.github/workflows/`.

| Ruta | Tamaño | Qué es |
|---|---|---|
| `README.md` | 535 B | Descripción de la plantilla y cómo usarla |
| `Dockerfile` | 242 B | Imagen base python:3.11-slim + make |
| `docker-compose.yml` | 128 B | Servicio `pva-paper`, `make repro` |
| `Makefile` | 285 B | Objetivos: repro, dev, test, lint, reproduce |
| `requirements.txt` | 28 B | 4 dependencias sin versión fijada |
| `.gitignore` | 22 B | `*.tar.gz`, `__pycache__/` |
| `data/GRACE_TN14_REAL_TEMPLATE.csv` | 331 B | 7 filas de datos C20 (2002–2023) |
| `data/README.md` | 86 B | Una línea que describe los datos |
| `scripts/repro.py` | 470 B | Lee el CSV, imprime resumen, escribe figura |
| `scripts/verify_data.py` | 370 B | Comprueba que el CSV existe y tiene ≥3 filas |
| `.github/workflows/pva.yml` | 339 B | CI: build docker + repro + verify |

Ausencias (SÉ, por listado de raíz y de cada carpeta):

- No hay `LICENSE`.
- No hay directorio `tests/` (el objetivo `test` del Makefile solo corre
  `verify_data.py`).
- No hay código de puntuación PVA: ningún archivo calcula un "PVA score".
- No hay figura real: `fig_C20.png` no existe en el repo; `repro.py` la
  escribiría como bytes `dummy` si se ejecutara.

Todos los archivos listados arriba fueron leídos íntegramente. Nada quedó
sin leer.
