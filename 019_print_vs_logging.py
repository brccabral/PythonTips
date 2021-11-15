# prefer to use logging
import logging

def dont_print():
    print("debug info")
    print("just some info")
    print("bad info")

def use_logging():
    logging.debug("debug info")
    logging.info("just some info")
    logging.error("error info")

level = logging.DEBUG
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=level)

dont_print()
use_logging()