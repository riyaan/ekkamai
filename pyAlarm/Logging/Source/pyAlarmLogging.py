import logging

class KivyLogging(object):

    LOCATION = "C:\\temp\\pyAlarmLog.txt"
    scriptName = ""
    logLevel = ""

    def __init__(self, logLevel, scriptFileName):
        logging.basicConfig(format='[%(asctime)s] - %(levelname)s : %(message)s', 
                            filename=self.LOCATION, level=logLevel)
        self.scriptName = scriptFileName
        self.logLevel = logLevel

    def Log(self, message):
        if self.logLevel == "DEBUG":
            logging.debug(("[{0}] - {1}").format(self.scriptName, message))
        elif self.logLevel == "INFO":
            logging.info(("[{0}] - {1}").format(self.scriptName, message))
        elif self.logLevel == "CRITICAL":
            logging.critical(("[{0}] - {1}").format(self.scriptName, message))      