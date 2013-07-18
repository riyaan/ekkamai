import os

from datetime import datetime

from HAL.Source.pyAlarmHAL import HAL
from Logging.Source.pyAlarmLogging import KivyLogging

class pyCore(object):
    """description of class"""

    LOG_LEVEL = "DEBUG"
    SCRIPT_FILE_NAME = os.path.basename(__file__)
    
    logger = ""

    def __init__(self):
        self.logger = KivyLogging(self.LOG_LEVEL, self.SCRIPT_FILE_NAME)

    def Poll(self):

        self.logger.Log("Start - Poll.")       

        hal = HAL()
        alarmList = hal.RetrieveAllAlarms()

        for alarm in alarmList:
            self.logger.Log(("Alarm name - {0}{1}Alarm sound - {2}").format(alarm.name, os.linesep, alarm.sound))
            
        self.logger.Log("End - Poll.")