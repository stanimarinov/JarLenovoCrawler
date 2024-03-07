""" module setup_logging """

import logging

def setup_logger(name, level):
    """
    Set up logger with name and logging level.
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    format_str = '%(name)s:%(levelname)s:%(message)s'
    formatter = logging.Formatter(format_str)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger