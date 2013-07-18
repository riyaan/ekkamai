import datetime
import formatter
import os

# using a package instead of adding multiple paths to PYTHONPATH
from Controller.Source.AlarmController import Alarm
from Domain.Source import pyAlarmAlarm
from Logging.Source.pyAlarmLogging import KivyLogging
from Core.Source.pyAlarmCore import pyCore

LOG_LEVEL = "DEBUG"
SCRIPT_FILE_NAME = os.path.basename(__file__)

ALARM_NAME = "myThirdAlarm"

# initialize the logger
logger = KivyLogging(LOG_LEVEL, SCRIPT_FILE_NAME)

logger.Log('Start - Main thread of execution.')

core = pyCore()
core.Poll()

v = raw_input("Press any key to exit ...")

#alarmController = Alarm()
#alarmList = alarmController.RetrieveAlarmList()
#for alarm in alarmList:    
#    logger.Log(("Alarm name - {0}{1}Alarm sound - {2}").format(alarm.name, os.linesep, alarm.sound))

#successfulRequest = alarmController.NewAlarmRequest(ALARM_NAME)

#successfulRequest = False

#if not successfulRequest:

#    alarmTime = datetime.datetime(2013, 7, 19, 5, 0, 0)
#    snoozeLength = datetime.time(0,15)

#    logger.Log('End - Main thread of execution.')
#    alarmController.SaveAlarm(ALARM_NAME, "Monday", alarmTime, "elixir", 5, snoozeLength, True, True)

#v = raw_input("Alarm creation in process...")