import os
import threading
import time

from datetime import datetime

from HAL.Source.pyAlarmHAL import HAL
from Logging.Source.pyAlarmLogging import KivyLogging

class pyCore(object):

    LOG_LEVEL = "DEBUG"
    SCRIPT_FILE_NAME = os.path.basename(__file__)
    
    logger = ""
    hal = ""

    def __init__(self):
        self.logger = KivyLogging(self.LOG_LEVEL, self.SCRIPT_FILE_NAME)    

    def Poll(self):

        self.logger.Log("Start - Poll.")
        self.hal = HAL()

        while True:
            t = threading.Timer(1, self.Processing)
            t.start()
            time.sleep(3)
                        
        self.logger.Log("End - Poll.")

    def Processing(self):

        self.logger.Log("Start - Processing")

        alarmList = self.hal.RetrieveAllAlarms()

        for alarm in alarmList:
            if alarm.time <= datetime.now() & alarm.
            self.logger.Log(("Alarm name - {0}Alarm sound - {1}").format(alarm.name, alarm.sound))

        self.logger.Log("End - Processing")