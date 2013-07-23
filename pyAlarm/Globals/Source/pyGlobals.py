from os import path

#def __init__():
global IS_RUNNING
IS_RUNNING = True

global ALARM_LOCATION
ALARM_LOCATION = "C:\\temp\\*.pkl"

global DEBUG_LOG_LEVEL
DEBUG_LOG_LEVEL = "DEBUG"

global INFO_LOG_LEVEL
INFO_LOG_LEVEL = "INFO"

global ERROR_LOG_LEVEL
ERROR_LOG_LEVEL = "ERROR"

global CRITICAL_LOG_LEVEL
CRITICAL_LOG_LEVEL = "CRITICAL"

global SCRIPT_FILE_NAME
SCRIPT_FILE_NAME = path.basename(__file__)

global LOGFILE_LOCATION
LOGFILE_LOCATION = "C:\\temp\\pyAlarmLog.txt"