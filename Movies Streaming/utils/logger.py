import logging
import os
from ..config import Config

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, Config.LOG_LEVEL))
    
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(Config.LOG_FILE), exist_ok=True)
    
    # File handler
    file_handler = logging.FileHandler(Config.LOG_FILE)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    logger.addHandler(file_handler)
    
    return logger
