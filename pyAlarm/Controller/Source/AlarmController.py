from os import path

from Domain.Source.pyAlarmAlarm import Alarm as DomainAlarm
from Domain.Source.pyAlarmAlarmDay import AlarmDay
from Exceptions.Source.pyException import *
from Globals.Source import pyGlobals
from HAL.Source import pyAlarmHAL
from Logging.Source.pyAlarmLogging import KivyLogging

class Alarm(object):

    LOG_LEVEL = "DEBUG"
    SCRIPT_FILE_NAME = path.basename(__file__)       

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
            exceptionMsg = "There is insufficient storage space available for alarm creation."
            self.logger.Log(exceptionMsg, pyGlobals.ERROR_LOG_LEVEL)
            raise InsufficientStorageSpaceAvailableException(exceptionMsg)

        # check if there is already a similarly named alarm
        if hal.IsAlarmNameAvailable(alarmName):
            self.logger.Log('Alarm name is available for use.')
        else:
            exceptionMsg = ("Alarm name '{0}' is already in use.").format(alarmName)
            self.logger.Log(exceptionMsg, pyGlobals.ERROR_LOG_LEVEL)
            raise AlarmNameInUseException(exceptionMsg)

    def SaveAlarm(self, alarmName, alarmDay, alarmTime, alarmSound, alarmVolume, snoozeLength, isRepeatable, isActive):       
        """
        Save an instance of the newly created alarm to the device storage.

        Args:
            alarmName: The name of the alarm.
            alarmDay: The day of the week the alarm should be activated. E.g Monday
            alarmTime: The time the alarm should be activated.
            alarmSound: The notification sound to be played when the alarm is active.
            alarmVolume: The volume for the notification sound.
            snoozeLength: The amount of time the alarm should snooze for.
            isRepeatable: Should the alarm repeat for the specified days and time.
            isActive: Is the alarm made active.

        """

        self.logger.Log('Begin - SaveAlarm.')

        alarmDay = AlarmDay(alarmDay, alarmTime)
        alarm = DomainAlarm(alarmName, alarmDay, alarmSound, alarmVolume, isRepeatable, alarmTime, isActive)

        hal = pyAlarmHAL.HAL()
        hal.StoreAlarm(alarm)

        self.logger.Log('End - SaveAlarm.')

        return True

    def Notify(self, alarm):
        # notify the UI
        
        self.logger.Log('Begin - Notify.')
        self.logger.Log('End - Notify.')