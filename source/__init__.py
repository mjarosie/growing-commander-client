import logging

from logging.config import dictConfig


def get_logger(name):
    logging_config = dict(
        version=1,
        formatters={
            'f': {
                'format': "{asctime} {name} {levelname:8s} {message}",
                'style': '{'
            }
        },
        handlers={
            'h': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG
            }
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
        disable_existing_loggers=False
    )

    dictConfig(logging_config)

    return logging.getLogger(name)
