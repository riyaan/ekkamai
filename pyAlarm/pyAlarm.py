import datetime, formatter, os, threading

# using a package instead of adding multiple paths to PYTHONPATH
from Controller.Source.AlarmController import Alarm
from Core.Source.pyAlarmCore import pyCore
from Domain.Source import pyAlarmAlarm
from Globals.Source import pyGlobals
from Logging.Source.pyAlarmLogging import KivyLogging

pyGlobals.IS_RUNNING = True

# initialize the logger
logger = KivyLogging(pyGlobals.LOG_LEVEL, pyGlobals.SCRIPT_FILE_NAME)

# main thread of execution
logger.Log('Start - Main thread of execution.')

#### Polling functionality - Start

def Poll():
    core = pyCore()
    core.Poll()

logger.Log("Configure 'Polling' thread")
pollingThread = threading.Thread(target=Poll,name="pollingThread")
pollingThread.start()
logger.Log("'Polling' thread has been started")

#### Polling functionality - End

logger.Log("Continuing 'Main' thread execution.")

### Alarm Creation Begin

alarmController = Alarm()

ALARM_NAME = "Ekkamai"
successfulRequest = alarmController.NewAlarmRequest(ALARM_NAME)

successfulRequest = False

if successfulRequest:

    alarmTime = datetime.datetime(2013, 7, 23, 5, 0, 0)
    snoozeLength = datetime.time(0,15)

    logger.Log('End - Main thread of execution.')
    alarmController.SaveAlarm(ALARM_NAME, "Monday", alarmTime, "If_Only", 5, snoozeLength, True, True)

### Alarm Creation End

v = raw_input("Press [p]roceed to continue or e[x]it to quit ...")

while v != "x":
    logger.Log(v)
    v = raw_input("Press [p]roceed to continue or e[x]it to quit ...")

pyGlobals.IS_RUNNING = False

logger.Log('End - Main thread of execution.')