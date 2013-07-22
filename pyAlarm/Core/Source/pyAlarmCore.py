import datetime, os, threading, time

from Controller.Source.AlarmController import Alarm
from Globals.Source import pyGlobals
from HAL.Source.pyAlarmHAL import HAL
from Logging.Source.pyAlarmLogging import KivyLogging

class pyCore(object):    
    
    logger = ""
    hal = ""

    def __init__(self):
        self.logger = KivyLogging(pyGlobals.LOG_LEVEL, pyGlobals.SCRIPT_FILE_NAME)    

    def Poll(self):
        self.logger.Log("Start - Poll.")
        self.logger.Log("Thread name: {0}".format(threading.currentThread().name))
        self.hal = HAL()        

        while pyGlobals.IS_RUNNING:
            t = threading.Timer(1, self.Processing)
            t.start()
            time.sleep(2)
                        
        self.logger.Log("End - Poll.")

    def Processing(self):

        self.logger.Log("Start - Processing")

        alarmList = self.hal.RetrieveAllAlarms()

        self.logger.Log("Number of alarms: {0}".format(len(alarmList)))

        for alarm in alarmList:
            d = datetime.datetime.now()
            if (alarm.time <= d) & (alarm.isActive == True):
                self.logger.Log(("Alarm name - {0}____Alarm time - {1}____Current time - {2}____Is Active? - {3}").
                                format(alarm.name, alarm.time, d, alarm.isActive))

                # notify that the alarm has sound
                alarmController = Alarm()
                alarmController.Notify(alarm)

        self.logger.Log("End - Processing")