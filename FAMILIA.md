# FAMILIA — pva-docker-template

Repo: `Jaime393/pva-docker-template`, rama `main`.
Leído en vivo 2026-11-09 ~07:07 -05.

## Familia PVA (ecosistema de validación)

Este repo es una pieza del ecosistema PVA (7 repos `pva-*` en Jaime393).
El vínculo verificado **dentro de este repo** es uno solo: el Makefile
intenta correr `pva-lint` en tres rutas (`python -m pva_lint.cli`,
`../pva-lint/cli.py`, `cli.py`) y, si no lo encuentra, sigue con
"pva-lint no encontrado, ok". Es decir: la plantilla **depende de
pva-lint solo si está al lado** (hermano en el mismo directorio); sin
él, el `repro` se declara OK igualmente.

Los demás hermanos, según la tarea de minería (no leídos por mí en
esta tanda; su contenido es NO SÉ para este archivo):

| Repo hermano | Papel según su README (muestreo del censo) |
|---|---|
| `pva-lint` | Linter PVA, score 0–1, transición de fase >0.999 |
| `pva-ledger` | Registro inmutable (Arweave + Zenodo DOI) |
| `pva-lean-bridge` | Puente LaTeX → Lean 4 |
| `pva-orchestrator` | Orquestador: encadena lint + docker + lean + ledger + swarm con un `pva.yml` |
| `pva-swarm` | Validación adversarial distribuida (FastAPI + SQLite) |
| `pva-api` | Un solo `app.py`, FastAPI o stdlib según disponibilidad |

El nombre del workflow (`.github/workflows/pva.yml`) coincide con el
`pva.yml` que lee el orquestador — NO SÉ si es el mismo formato o solo
el mismo nombre.

## Relaciones fuera de PVA

- **miu-v150-***: los 4 README de esa familia citan los mismos datos
  ("TN-14 GSFC SLR", DOI 10.1029/2019GL085488, Ktau 0.3644, r=-0.868)
  que este repo. El dato que este repo trae en 7 filas, la familia
  v150 lo cita en 257 filas. NO SÉ si comparten fuente o solo la cita.
- **MIU en general**: el README cierra con "ρ(x)>0" y el commit con
  "ρ(x)>0"; la plantilla es MIU por firma, no por contenido técnico
  propio.
- **DOI externo**: 10.1029/2019GL085488 (Loomis et al. 2020, NASA GSFC
  SLR) es la única fuente externa real citada, verificada en web
  2026-11-09.

## Posición en la familia

Es la pieza de **reproducibilidad** (Bloque: empaquetar un paper para
que corra con un comando). Pero su "repro" no reproduce nada medible:
la figura es `dummy`, el score no se calcula, y la verificación de
datos solo exige ≥3 filas. La plantilla promete más de lo que su
código hace — el hueco es de ejecución, no de intención.
