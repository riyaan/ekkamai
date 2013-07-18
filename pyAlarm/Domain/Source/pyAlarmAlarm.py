from datetime import datetime

from Domain.Source.pyAlarmAlarmDay import AlarmDay

class Alarm(object):

    name = ""
    alarmDay = ""
    sound = ""
    volume = 0
    isRepeatable = False
    time = datetime.now()

    def __init__(self):
        name = ""
        alarmDay = AlarmDay("Sunday", datetime.now())
        sound = ""
        volume = 0
        isRepeatable = False
        time = datetime.now()

    def __init__(self, name, alarmDay, sound, volume, isRepeatable, time):
        self.name = name
        self.alarmDay = alarmDay
        self.sound = sound
        self.volume = volume
        self.isRepeatable = isRepeatable
        self.time = time