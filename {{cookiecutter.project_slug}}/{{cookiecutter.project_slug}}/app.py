from envparse import env
from loguru import logger

from .pkg_utils import get_title_description, get_version
from .setup_logger import setup_logger


env.read_envfile()
DEBUG = env.bool("DEBUG", default=False)

class SomeApp:
    pass

def build_app(debug=False) -> SomeApp:
    """Build the application."""
    version = get_version()
    title = get_title_description()
    setup_logger(debug=debug or DEBUG)
    logger.debug("Welcome to the application {}. {}".format(*title))
    logger.debug(f"Building application version {version} started...")
    # TODO create app instance
    app = SomeApp()
    return app
