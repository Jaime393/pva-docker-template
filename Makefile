repro:
	python3 scripts/repro.py

dev:
	bash

test:
	python3 -m unittest discover -s tests -v

lint:
	python3 scripts/verify_data.py

reproduce:
	python3 scripts/repro.py
