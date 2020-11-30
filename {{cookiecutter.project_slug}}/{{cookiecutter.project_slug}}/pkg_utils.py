from pathlib import Path
from typing import Tuple

import toml


PKG_ROOT = Path(__file__).parents[1]


def get_version() -> str:
    """Get the current package version from pyproject.toml."""
    with open(PKG_ROOT / "pyproject.toml") as f:
        pyproject = toml.loads(f.read())
    return pyproject["tool"]["poetry"]["version"]


def get_title_description() -> Tuple[str, str]:
    """Get the package title from pyproject.toml."""
    with open(PKG_ROOT / "pyproject.toml") as f:
        pyproject = toml.loads(f.read())
    return (
        " ".join(
            token.capitalize()
            for token in pyproject["tool"]["poetry"]["name"].split("-")
        ),
        pyproject["tool"]["poetry"]["description"],
    )
