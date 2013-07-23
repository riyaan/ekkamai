import logging

from Globals.Source import pyGlobals

class KivyLogging(object):

    def __init__(self, logLevel, scriptFileName):
        logging.basicConfig(format='[%(asctime)s] - %(levelname)s : %(message)s', 
                            filename=pyGlobals.LOGFILE_LOCATION, level=logLevel)
        self.scriptName = scriptFileName
        self.logLevel = logLevel

    def Log(self, message, logLevel=""):
        """
        Write the specified message to a log file.
        """

        if logLevel == "":
            logLevel = self.logLevel

        if logLevel == "DEBUG":
            logging.debug(("[{0}] - {1}").format(self.scriptName, message))
        elif logLevel == "CRITICAL":
            logging.critical(("[{0}] - {1}").format(self.scriptName, message))
        elif logLevel == "ERROR":
            logging.error(("[{0}] - {1}").format(self.scriptName, message))
        elif logLevel == "INFO":
            logging.info(("[{0}] - {1}").format(self.scriptName, message))        