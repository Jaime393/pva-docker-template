repro:
	python scripts/repro.py
	python -m pva_lint.cli --json || python ../pva-lint/cli.py --json || python cli.py --json || echo "pva-lint no encontrado, ok"

dev:
	bash

test:
	python scripts/verify_data.py

lint:
	python scripts/verify_data.py

reproduce:
	python scripts/repro.py
