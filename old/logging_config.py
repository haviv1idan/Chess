import logging
import logging.config
import colorlog

def setup_logger():
    log_colors = {
        'DEBUG': 'green',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
    
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_colors=log_colors
    )
    
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'colored': {
                '()': colorlog.ColoredFormatter,
                'format': "%(log_color)s%(asctime)s|%(name)s| %(levelname)s| %(message)s",
                'log_colors': log_colors
            },
            'standard': {
                'format': '%(asctime)s|%(name)s|%(levelname)s|%(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'standard',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True
            },
        }
    })

# Call setup_logger to configure the logger when the module is imported
setup_logger()

# Function to get the configured logger
def get_logger(name):
    return logging.getLogger(name)
