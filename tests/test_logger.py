# unit test file for logger.py 
# logger.py is to initialize the logging setup
import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
import os
from src import logger

class TestLogger(unittest.TestCase):
    def test_logDirectory_creation(self):
        '''Able to create root directory for storing all the logs'''
        with patch("os.makedirs") as mock_makedirs:
            logger.LOG_DIR = "test_log_dir"
            logger.setUp_logger()
            mock_makedirs.assert_called_once_with("test_log_dir", exist_ok=True)


