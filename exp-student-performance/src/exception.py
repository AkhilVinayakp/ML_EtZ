## defining custom exceptions

import sys

class Error_info(Exception):
    '''
    Handling error in the scripts
    '''
    def __init__(self, err_msg:str, err_info:sys) -> None:
        super().__init__(err_msg)
        self.err_msg = Error_info.error_parser(error=err_msg, err_dt=err_info)
    def __str__(self) -> str:
        return self.err_msg

    @staticmethod
    def error_parser(error:str, err_dt:sys)->str:
        ''' 
        Generate error message
        Args: 
            error: error message string
            err_dt: error info object
        Returns: 
            error_msg: formatted string
        Raises: 
            null
        '''
        _, _, exec_info = err_dt.exc_info()
        f_name:str = exec_info.tb_frame.f_code.co_filename
        l_no:int = exec_info.tb_lineno
        error_msg = f"Error in script: {f_name} in line {l_no} message:{error}."
        return error_msg
    