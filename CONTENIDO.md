# CONTENIDO — pva-docker-template

Repo: `Jaime393/pva-docker-template`, rama `main`.
Leído en vivo 2026-11-09 ~07:07 -05. Todos los números abajo se
calcularon o se leyeron de los archivos del repo, no de memoria.

## Qué hace

Es una plantilla Docker + Make para reproducir un paper con un solo
comando (`make repro`). El flujo real, según los archivos:

1. `Dockerfile`: imagen `python:3.11-slim`, instala `make`, instala
   `requirements.txt` (requests, click, numpy, pandas — sin versión
   fijada), copia el repo, `CMD ["make", "repro"]`.
2. `Makefile` → `repro`: corre `scripts/repro.py` y luego intenta
   `pva-lint` en tres rutas (`python -m pva_lint.cli`, `../pva-lint/cli.py`,
   `cli.py`); si ninguna existe, imprime "pva-lint no encontrado, ok".
3. `scripts/repro.py`: lee el CSV, imprime filas y último C20, escribe
   una figura.
4. `scripts/verify_data.py`: comprueba que el CSV existe y tiene ≥3 filas.

## Los datos (verificados en el archivo)

`data/GRACE_TN14_REAL_TEMPLATE.csv`: cabecera `date,C20,source` + **7
filas** (no 221; ver discrepancia abajo).

| Fecha | C20 | source |
|---|---|---|
| 2002-04-18 | -0.0004847000261009811 | GRACE_TN14 |
| 2003-06-10 | -0.0004846999 | GRACE_TN14 |
| 2005-01-20 | -0.0004846995 | GRACE_TN14 |
| 2010-08-15 | -0.0004846992 | GRACE_TN14 |
| 2015-03-10 | -0.0004846998 | GRACE_TN14 |
| 2020-11-05 | -0.0004847001 | GRACE_TN14 |
| 2023-03-15 | -0.0004847000261009811 | GRACE_TN14 |

Cálculos propios sobre esas 7 filas (2026-11-09):

- Media C20: **-0.00048469979317170887** (≈ -4.8470e-04).
- Mínimo: -0.0004847001; máximo: -0.0004846992.
- Primera y última fila tienen el **mismo valor exacto**
  (-0.0004847000261009811): la última fila duplica el valor de la
  primera. NO SÉ por qué.

## Lo que el repo afirma y su estado

| Afirmación | Dónde | Estado |
|---|---|---|
| DOI 10.1029/2019GL085488 | README, data/README, verify_data.py | **Verificado real**: Loomis et al. 2020, "Replacing GRACE/GRACE-FO C30 With Satellite Laser Ranging", *Geophys. Res. Lett.* 47(3), e2019GL085488 (búsqueda web 2026-11-09). El DOI es del paper SLR C20/C30 de NASA GSFC, no de este CSV. |
| C20 ≈ -0.0004846999 | README, data/README, commit | **Coherente con el CSV**: la media de las 7 filas es -0.0004846998; los valores rondan -0.0004847. |
| Ktau 0.3644, r=-0.868, sigma_ref 1.35e-10 | README, repro.py | **Literales, no calculados**: `repro.py` los imprime como texto fijo. El CSV no tiene columna LOD ni nada con lo que calcular una correlación r. NO SÉ de dónde salen. |
| "221 filas IERS C04" | data/README.md | **Falso contra el archivo**: el CSV tiene 7 filas y fuente `GRACE_TN14`, no IERS C04. Tres números distintos circulan para este mismo dato: 7 (el archivo), 221 (data/README), 257 (los README de miu-v150-*, que citan "TN-14 GSFC SLR 257 filas"). NO SÉ cuál es el real fuera de este repo. |
| "PVA score esperado: 1.0" | README | **Esperado, no medido**: ningún archivo calcula un score. |
| "figura fig_C20.png generada" | repro.py | **Falsa como figura**: el script escribe bytes `dummy` y lo anuncia él mismo ("generada (dummy)"). No hay imagen real. |
| Makefile con 5 objetivos | README, Makefile | **SÉ**: repro, dev, test, lint, reproduce existen. `test` y `lint` hacen lo mismo (correr verify_data.py). |

## Lo que NO se sabe

- Si `docker build` y `make repro` funcionan (no se ejecutaron).
- Si el CI de `.github/workflows/pva.yml` pasó alguna vez (no se
  consultaron los runs; además el paso Verify no tumba el trabajo).
- De dónde salen Ktau 0.3644, r=-0.868 y sigma_ref 1.35e-10.
- Por qué data/README dice 221 filas IERS C04 cuando el CSV tiene 7
  filas GRACE_TN14.
- Por qué la última fila duplica el valor C20 de la primera.
