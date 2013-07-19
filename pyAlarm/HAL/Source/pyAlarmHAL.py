import glob
import pickle

from os import path

from Logging.Source.pyAlarmLogging import KivyLogging

class HAL(object):
    
    ALARM_LOCATION = "C:\\temp\\*.pkl"
    LOG_LEVEL = "DEBUG"
    SCRIPT_FILE_NAME = path.basename(__file__)
    
    logger = ""

    def __init__(self):
        self.logger = KivyLogging(self.LOG_LEVEL, self.SCRIPT_FILE_NAME)

    def IsStorageSpaceSufficient(self):
        # TODO: Check if device has sufficient storage
        return True

    def IsAlarmNameAvailable(self, alarmName):
        # TODO: Check if alarm name is available
        return True

    def RetrieveAllAlarms(self):
        # deserialize objects and return list

        self.logger.Log("Start - Retrieving a list of alarms.")

        dirList = glob.glob(self.ALARM_LOCATION)

        self.logger.Log(("Number of items in directory - {0}.").format(len(dirList)))

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

        filePath = "C:\\temp\\"+alarm.name+".pkl"
        self.Serialize(alarm, filePath)

        self.logger.Log("End - StoreAlarm.")