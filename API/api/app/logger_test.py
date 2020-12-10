import logging, sys

class SingleLevelFilter(logging.Filter):
    def __init__(self, passlevel, reject):
        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record):
        if self.reject:
            return (record.levelno != self.passlevel)
        else:
            return (record.levelno == self.passlevel)

# h1 = logging.StreamHandler(sys.stdout)
# f1 = SingleLevelFilter(logging.INFO, False)
# h1.addFilter(f1)
rootLogger = logging.getLogger()
# rootLogger.addHandler(h1)
h2 = logging.StreamHandler(sys.stderr)
f2 = SingleLevelFilter(logging.INFO, True)
h2.addFilter(f2)
rootLogger.addHandler(h2)
logger = logging.getLogger("my.logger")
logger.setLevel(logging.DEBUG)
logger.debug("A DEBUG message")
logger.info("An INFO message")
logger.warning("A WARNING message")
logger.error("An ERROR message")
logger.critical("A CRITICAL message")