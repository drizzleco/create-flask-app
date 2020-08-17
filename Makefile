.PHONY: install
install: 
	python3 -m venv .env; \
	. .env/bin/activate; \
	pip install -e .;
