import logging
import sys

from loguru import logger


class InterceptHandler(logging.Handler):
    """Handler which forwards all records to loguru logger."""

    def emit(self, record: logging.LogRecord) -> None:
        """Reemit the record to loguru logger."""
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back  # type: ignore
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logger(log_to_file: bool = False, debug: bool = False) -> None:
    """Setup app logger."""
    logging.getLogger().handlers = [InterceptHandler()]

    stdout_handler = {
        "sink": sys.stdout,
        "level": logging.DEBUG if debug else logging.INFO,
    }
    if debug:
        stdout_handler.update({"backtrace": True, "diagnose": True})
    handlers = [stdout_handler]
    if log_to_file:
        handlers.append(
            {
                "sink": "./logs/logger_history_{time}.log",
                "rotation": "2 MB",
                "retention": "10 days",
                "level": logging.DEBUG if debug else logging.INFO,
            }
        )
    logger.configure(handlers=handlers)
    logger.debug("Logger configured successfully.")
    logger.debug(f"DEBUG is {debug}")
