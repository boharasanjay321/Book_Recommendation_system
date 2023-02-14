from Book_System.logger import logging
from Book_System.exception import SensorException
import sys


def test_logger_and_exception():
     try:
          logging.info("start the test logger")
          result=3/0

          print(result)
          logging.info("stopping the test logger")
     except Exception as e:
          logging.debug(str(e))
          raise SensorException(e, sys)




if __name__=="__main__":
     try:
          test_logger_and_exception()
     except Exception as e:
          print(e)