import logging
from config.config import Config

# def setup_logger(app):

#     # Create logger
#     file_handler = logging.FileHandler(Config.LOG_DIR)
#     file_handler.setLevel(logging.DEBUG)
    
#     # Define log message format
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
#     file_handler.setFormatter(formatter)

#     # Attach handler to logger
#     app.logger.addHandler(file_handler)
#     # app.logger.setLevel(logging.DEBUG)
#     app.logger.info("Logger initialized")

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()
        ]
    )