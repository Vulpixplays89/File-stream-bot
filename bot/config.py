from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "26222466"))
    API_HASH = env.get("TELEGRAM_API_HASH", "9f70e2ce80e3676b56265d4510561aef")
    OWNER_ID = int(env.get("OWNER_ID", "6897739611"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "HHTGFilezDLBot")
    BOT_TOKEN = "7770146776:AAFnkdNxEGZE4VjyjONz7PjuXq79CGo1t1o"
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1002635785984"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 4))

class Server:
    BASE_URL = env.get("BASE_URL", "https://filestr-bot-09bc2a39ec69.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 3000))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
