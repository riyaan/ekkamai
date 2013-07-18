from os import path

from Domain.Source.pyAlarmAlarm import Alarm as DomainAlarm
from Domain.Source.pyAlarmAlarmDay import AlarmDay
from HAL.Source import pyAlarmHAL
from Logging.Source.pyAlarmLogging import KivyLogging

class Alarm(object):

    LOG_LEVEL = "DEBUG"
    SCRIPT_FILE_NAME = path.basename(__file__)
    
    logger = ""

    def __init__(self):
        self.logger = KivyLogging(self.LOG_LEVEL, self.SCRIPT_FILE_NAME)

    def RetrieveAlarmList(self):
        self.logger.Log('Start - Getting a list of alarms.')

        hal = pyAlarmHAL.HAL()

        self.logger.Log('End - Getting a list of alarms.')

        return hal.RetrieveAllAlarms()

    def NewAlarmRequest(self, alarmName):
        # check if the device has sufficient storage space
        hal = pyAlarmHAL.HAL()
        if hal.IsStorageSpaceSufficient():
            self.logger.Log('There is sufficient space.')
        else:
            return False

        # check if there is already a similarly named alarm
        if hal.IsAlarmNameAvailable(alarmName):
            self.logger.Log('Alarm name is available for use.')
        else:
            self.logger.Log('Alarm name is in use.')
            return False

    def SaveAlarm(self, alarmName, alarmDay, alarmTime, alarmSound, alarmVolume, snoozeLength, isRepeatable, isActive):       

        self.logger.Log('Begin - SaveAlarm.')

        alarmDay = AlarmDay(alarmDay, alarmTime)
        alarm = DomainAlarm(alarmName, alarmDay, alarmSound, alarmVolume, isRepeatable, alarmTime, isActive)

        hal = pyAlarmHAL.HAL()
        hal.StoreAlarm(alarm)

        self.logger.Log('End - SaveAlarm.')

        return True