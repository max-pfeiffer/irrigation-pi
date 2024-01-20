SHELL=/bin/bash

poetry_install:
	curl -sSL https://install.python-poetry.org | python -
	cat "export ~/local/bin:$PATH" >> .bashrc

install_backend_dependencies:
	cd backend
	poetry install --no-dev --no-root
	cd ..

update_backend_dependencies:
	cd backend
	poetry update --no-dev --no-root
	cd ..

run_backend_tests:
	cd backend
	python -m pytest
	cd ..
