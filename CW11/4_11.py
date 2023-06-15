import logging


def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s;%(levelname)s;%(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('application.log')
        ]
        
    )

    logger = logging.getLogger("test")
    
    return logger


if __name__ == "__main__":
    logger = setup_logger()
    logger.info("This is an info log")
    logger.warning("This is a warning message")
    logger.error("This is an error")