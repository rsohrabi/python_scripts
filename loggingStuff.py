# logging stuff for use as general template.
import logging
logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s, %(asctime)s, %(message)s")
logging.debug("debug statement")
logging.info("This is informative")
logging.error("Something went wrong.")
