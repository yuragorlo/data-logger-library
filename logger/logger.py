import os
import logging
from uvicorn.config import LOGGING_CONFIG

LOG_FORMAT = "[%(asctime)s] [0] [%(levelname)s] %(message)s"

logger = logging.getLogger("databases")
logger.setLevel(logging.DEBUG)

LOGGING_CONFIG["formatters"]["default"]["fmt"] = LOG_FORMAT
LOGGING_CONFIG["formatters"]["access"]["fmt"] = LOG_FORMAT

try:
    DEFAULT_NAME = "com.newagesol.{}".format(os.environ["NAS_SERVICE"])
except KeyError:
    DEFAULT_NAME = "local"


def get_logger(log_name=DEFAULT_NAME):
    log = logging.getLogger(log_name)
    log.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    fmt_essential = LOG_FORMAT
    stream_handler.setFormatter(logging.Formatter(fmt_essential))
    log.addHandler(stream_handler)

    return log
