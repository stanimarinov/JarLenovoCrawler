""" Module for loading specified file."""

import configparser
import os
import logging

from setup_logging import setup_logger

logger = setup_logger('config_loader', logging.DEBUG)

class ConfigError(Exception):
    """Custom exception for errors to configuration loading and parsing."""

    def __init__(self, message):
        """ Initializes a new ConfigError object with message."""
        super().__init__(message)


def load_config(config_file, section)->dict:
    """Loads configuration for handling potential errors."""

    config = configparser.ConfigParser()

    try:
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Error: Configuration file '{config_file}' not found")

        config.read(config_file)

        return dict(config[section])
    except KeyError as e:
        message = f"Missing configuration section: {section} in {config_file}"
        logger.error(message)
        raise ConfigError(message) from e
    except FileNotFoundError as e:
        message = f"Error: CONFIGURATION FILE '{os.path.abspath(config_file)}' not found"
        logger.error(message)
        raise ConfigError(message) from e
    except configparser.Error as e:
        message = f"Error reading configuration file: {e}"
        logger.error(message)
        raise ConfigError(message) from e