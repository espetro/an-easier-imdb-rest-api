from typing import Optional

import logging
import sys

class CustomLogger:
    def __init__(self, name: str, output: Optional[str] = None):
        self.logger = logging.getLogger(name)
        
        if output:
            warn_handler = logging.FileHandler(output)
            error_handler = logging.FileHandler(output)
        else:
            warn_handler = logging.StreamHandler()
            error_handler = logging.StreamHandler(output)
        
        warn_handler.setLevel(logging.WARNING)
        error_handler.setLevel(logging.ERROR)
        
        self.logger.addHandler(warn_handler)
        self.logger.addHandler(error_handler)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def fatal(self, msg: str):
        self.logger.fatal(msg)
        sys.exit(1)