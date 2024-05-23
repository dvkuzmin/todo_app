logger_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'file_formatter': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO'
        },
        'filehandler': {
            'class': 'logging.FileHandler',
            'formatter': 'file_formatter',
            'mode': 'w',
            'level': 'INFO',
            'filename': 'events.log',
        }
    },
    'loggers': {
        '': {
            'formatter': 'default',
            'handlers': ['default', 'filehandler'],
            'propagate': False,
            'level': 'INFO'
        },
        'sqlalchemy': {
            'propagate': False
        }
    }
}
