.PHONY: \
	install \
	lint \
	list-outdated \
	test \
	test-only \
	bump_dependencies \

PRE_COMMIT ?= pre-commit
POETRY ?= poetry
PYTHON ?= $(POETRY) run python

all: install


install: .install-pre-commit .install

.install-pre-commit:
	$(PRE_COMMIT) install --install-hooks

.install:
	cp .env.example .env
	$(POETRY) install

lint:
	$(PRE_COMMIT) run --all-files

list-outdated:
	$(POETRY) show -o


test: lint test-only


test-only: .install
	$(POETRY) run pytest

bump_dependencies:
	$(POETRY) update
	$(PRE_COMMIT) autoupdate
	@printf "\nThe environment still has the following outdated dependencies:\n"
	@$(POETRY) show -o
	@printf "\nCheck if it can be resolved in the pyproject.toml tool.poetry.dependencies and tool.poetry.dependencies-dev"

clean:
	find -name "__pycache__" | xargs rm -frv {}
	rm -frv logs
	rm -frv .mypy_cache
	rm -frv .pytest_cache
	rm -frv .coverage
