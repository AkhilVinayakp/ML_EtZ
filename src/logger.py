import datetime
import logging
import os

LOG_DIR = os.path.join(os.getcwd(), "logs")
class Mylogger:
    def __init__(self) -> None:
        '''
        initialize the logger functionalities
        '''
        # load the file name
        self.file_name = f"{datetime.now().strftime('%d_%m_%Y')}.log"