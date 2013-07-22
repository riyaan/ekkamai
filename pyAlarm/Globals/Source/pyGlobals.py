from os import path

#def __init__():
global IS_RUNNING
IS_RUNNING = True

global ALARM_LOCATION
ALARM_LOCATION = "C:\\temp\\*.pkl"

global LOG_LEVEL
LOG_LEVEL = "DEBUG"

global SCRIPT_FILE_NAME
SCRIPT_FILE_NAME = path.basename(__file__)