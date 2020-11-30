# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Development

### Required dependencies

- **poetry** - (https://python-poetry.org/docs/#installation) and
- **pre-commit** - (https://pre-commit.com/#install)

Copy environment file and adjust based on your needs:
```bash
cp .env.example .env
```

### Create development environment

```bash
make install
```

### Running tests and linters

```bash
make test
```
