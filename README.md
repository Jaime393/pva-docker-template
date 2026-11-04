# pva-docker-template

Plantilla de reproducción de un resumen CSV determinista. El recorrido local valida estructura y resume los valores presentes; no acredita que la muestra provenga de GRACE ni reproduce una hipótesis física.

```bash
make reproduce
make test
python3 scripts/repro.py --data data/GRACE_TN14_REAL_TEMPLATE.csv
```

La salida `pva.csv-summary/v1` incluye SHA-256 de los datos, fechas, número de registros y estadísticas descriptivas. No escribe un PNG ficticio, constantes Ki/r como resultados calculados ni un score científico.

Dockerfile y compose se conservan como rutas de empaquetado. Esta revisión fue probada en Python local; no se afirma construcción o ejecución Docker cuando el runtime no está disponible.
