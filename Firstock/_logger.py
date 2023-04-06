import sys 
import logging
import datetime as dt

class Logger:
    def __init__(self,name='CUSTOM_LOGGER'):
       
        self._format = '%(asctime)s : %(levelname)s | FILENAME : %(module)s | FUNCTION : %(funcName)s | LINE : %(lineno)d | MESSAGE: %(message)s'
        self._level = logging.INFO
        
        self._stdout_handler = logging.StreamHandler(sys.stdout)
        self._stdout_handler.setLevel(logging.DEBUG)
        self._stdout_handler.setFormatter(logging.Formatter(self._format))

        self._stderr_handler = logging.StreamHandler(sys.stderr)
        self._stderr_handler.setLevel(logging.WARNING)
        self._stderr_handler.setFormatter(logging.Formatter(self._format))

        self._output_file_handler = logging.FileHandler('firstock_output.log')
        self._output_file_handler.setLevel(logging.DEBUG)
        self._output_file_handler.setFormatter(logging.Formatter(self._format))

        self._error_file_handler = logging.FileHandler('firstock_error.log')
        self._error_file_handler.setLevel(logging.WARNING)
        self._error_file_handler.setFormatter(logging.Formatter(self._format))

        logging.basicConfig(level=self._level,handlers=[self._stdout_handler,self._stderr_handler,self._output_file_handler,self._error_file_handler])
        self._logger = logging.getLogger(name)

    def info(self,message):
        self._logger.info(message)
    
    def debug(self,message):
        self._logger.debug(message)

    def error(self,message):
        self._logger.error(message)

    def warning(self,message):
        self._logger.warning(message)

    def trace(self,message):
        self._logger.error(message,exc_info=True)

    def critical(self,message):
        self._logger.critical(message,exc_info=True)

log = Logger()