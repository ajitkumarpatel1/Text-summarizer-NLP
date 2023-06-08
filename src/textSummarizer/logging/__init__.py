import os
import sys
import logging

# formating the logging information for debugging
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# enitializing a log folder to store logging information
log_dir = "logs"
# defining the fath for logging information
log_filepath = os.path.join(log_dir,"running_logs.log")
# defining the diractory for logging information
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")