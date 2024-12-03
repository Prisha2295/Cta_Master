import unittest
import logging
import inspect

class logs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(__name__)
        if not cls.logger.handlers:
            cls.logger.setLevel(logging.INFO)
            fileHandler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            fileHandler.setFormatter(formatter)
            cls.logger.addHandler(fileHandler)

    def get_log(self):
        return self.logger
