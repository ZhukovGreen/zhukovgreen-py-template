import click

from {{cookiecutter.project_slug}}.app import build_app


@click.command()
@click.option("-v", "--verbose", count=True, help="Verbosity of the tool")
def cli(verbose: bool) -> None:
    """Application to do something."""
    # TODO Adjust the docstring
    build_app(debug=verbose)


