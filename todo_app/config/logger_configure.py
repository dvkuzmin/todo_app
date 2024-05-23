import logging.config

from .logger_settings import logger_config


def setup_logger():
    logging.config.dictConfig(logger_config)


setup_logger()
