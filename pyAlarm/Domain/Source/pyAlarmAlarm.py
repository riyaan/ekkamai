from datetime import datetime

from Domain.Source.pyAlarmAlarmDay import AlarmDay

class Alarm(object):

    name = ""
    alarmDay = ""
    sound = ""
    volume = 0
    isRepeatable = False
    time = datetime.now()
    isActive = False

    def __init__(self):
        self.name = ""
        self.alarmDay = AlarmDay("Sunday", datetime.now())
        self.sound = ""
        self.volume = 0
        self.isRepeatable = False
        self.time = datetime.now()
        self.isActive = False

    def __init__(self, name, alarmDay, sound, volume, isRepeatable, time, isActive):
        self.name = name
        self.alarmDay = alarmDay
        self.sound = sound
        self.volume = volume
        self.isRepeatable = isRepeatable
        self.time = time
        self.isActive = isActive