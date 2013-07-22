import glob, pickle

from Globals.Source import pyGlobals
from Logging.Source.pyAlarmLogging import KivyLogging

class HAL(object):        

    PARENT_DIRECTORY = "C:\\temp\\"
    EXTENSION = ".pkl"

    def __init__(self):
        self.logger = KivyLogging(pyGlobals.LOG_LEVEL, pyGlobals.SCRIPT_FILE_NAME)

    def IsStorageSpaceSufficient(self):
        # TODO: Check if device has sufficient storage
        return True

    def IsAlarmNameAvailable(self, alarmName):
        # TODO: Check if alarm name is available

        self.logger.Log("Start - IsAlarmNameAvailable")

        dirList = glob.glob(pyGlobals.ALARM_LOCATION)

        for item in dirList:           
            self.logger.Log(item)
            if not alarmName in item:
                self.logger.Log("Not found.")
            else:
                self.logger.Log("Found.")

        self.logger.Log("End - IsAlarmNameAvailable")

        return True

    def RetrieveAllAlarms(self):
        # deserialize objects and return list

        self.logger.Log("Start - Retrieving a list of alarms.")

        dirList = glob.glob(pyGlobals.ALARM_LOCATION)

        self.logger.Log(("Number of alarms in directory - {0}.").format(len(dirList)))

        alarmList = list()
        for i in range(0, len(dirList)):
             self.logger.Log(("Item - {0}.").format(i))
             object = self.Deserialize(dirList[i])
             self.logger.Log(("Alarm Name: {0}.").format(object.name))

             alarmList.append(object)

        self.logger.Log("End - Retrieving a list of alarms.")

        return alarmList

    def Serialize(self, object, filePath): 
        with open(filePath, "wb") as output:
            pickle.dump(object, output)

    def Deserialize(self, filePath):

        self.logger.Log("Start - Deserialize 'pickle'.")

        with open(filePath, "rb") as output:
            object = pickle.load(output)
            
        self.logger.Log("End - Deserialize 'pickle'.")

        return object

    def StoreAlarm(self, alarm):

        self.logger.Log("Start - StoreAlarm.")

        filePath = self.PARENT_DIRECTORY+alarm.name+self.EXTENSION
        self.Serialize(alarm, filePath)

        self.logger.Log("End - StoreAlarm.")