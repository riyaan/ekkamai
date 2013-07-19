import datetime
import formatter, os, threading

# using a package instead of adding multiple paths to PYTHONPATH
from Controller.Source.AlarmController import Alarm
from Core.Source.pyAlarmCore import pyCore
from Domain.Source import pyAlarmAlarm
from Logging.Source.pyAlarmLogging import KivyLogging

LOG_LEVEL = "DEBUG"
SCRIPT_FILE_NAME = os.path.basename(__file__)
ALARM_NAME = "myThirdAlarm"

# initialize the logger
logger = KivyLogging(LOG_LEVEL, SCRIPT_FILE_NAME)

# main thread of execution
logger.Log('Start - Main thread of execution.')
logger.Log("Thread name: {0}".format(threading.currentThread().name))

#### Polling functionality - Start
def Poll():
    core = pyCore()
    core.Poll()

logger.Log("Configure 'Polling' thread")
pollingThread = threading.Thread(target=Poll,name="pollingThread")
pollingThread.start()
logger.Log("'Polling' thread has been started")

logger.Log("Continuing 'Main' thread execution.")

#### Polling functionality - End

#alarmController = Alarm()
#alarmList = alarmController.RetrieveAlarmList()
#for alarm in alarmList:    
#    logger.Log(("Alarm name - {0}{1}Alarm sound - {2}").format(alarm.name, os.linesep, alarm.sound))

#successfulRequest = alarmController.NewAlarmRequest(ALARM_NAME)

#successfulRequest = False

#if not successfulRequest:

#    alarmTime = datetime.datetime(2013, 7, 17, 5, 0, 0)
#    snoozeLength = datetime.time(0,15)

#    logger.Log('End - Main thread of execution.')
#    alarmController.SaveAlarm(ALARM_NAME, "Monday", alarmTime, "dynamo", 5, snoozeLength, True, True)



v = raw_input("Press any key to exit ...")


logger.Log('End - Main thread of execution.')