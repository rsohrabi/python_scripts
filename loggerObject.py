# logger objects
import logging
logger = logging.getLogger()

# TODO: Change the log file name to what is needed.
log_file_handler = logging.FileHandler("mylog.txt")
logger.addHandler(log_file_handler)
logger.debug("debug on the way")
logger.warning("Possible issues")
hand = logger.hasHandlers()

# test to make sure it is working.
print("has handlers: %s" % hand)
logger.error("had handlers %s", hand)
