import unittest
import logging
import inspect

class logs(unittest.TestCase):
    def test_log(self):
        
        loggerName = inspect.stack()[1][3]
        self.logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('/home/praveenyadav/Desktop/test-automation/Performance/performace.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        self.logger.addHandler(fileHandler)  # filehandler object

        self.logger.setLevel(logging.INFO)
        return

        
