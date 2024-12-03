import logging
import os


class Logs:
    @staticmethod
    def loggen(test_case_name):
        log_dir = os.path.join(os.getcwd(), '../Logs', test_case_name)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, f'{test_case_name}.log')
        logger = logging.getLogger(test_case_name)
        fileHandler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger