import logging
import os


   
def get_logger(test_name):
    
    # Define the log directory and file path dynamically based on the test name
    log_directory = os.path.join(os.path.dirname(__file__), '../Logs')
    log_file = os.path.join(log_directory, f'{test_name}.log')

    # Create the log directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Set up the logger with a unique name for each test script
    logger = logging.getLogger(test_name + 'Logger')  # Unique logger name based on the test name
    logger.setLevel(logging.INFO)

    # Remove all handlers associated with the logger if they exist
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler for logging to a separate file for each test
    fileHandler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(fileHandler)

    return logger
