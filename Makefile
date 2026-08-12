run:
	uv run python -m personaos.main

doctor:
	uv run python scripts/doctor.py

lint:
	uv run ruff check .

format:
	uv run ruff format .

fix:
	uv run ruff check --fix .

test:
	uv run pytest

precommit:
	uv run pre-commit run --all-files
