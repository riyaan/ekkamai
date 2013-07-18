from datetime import datetime

class AlarmDay(object):

    day = ""
    time = datetime.now()
    
    def __init__(self):
        self.day = "Sunday"
        self.time = datetime.now()         

    def __init__(self, day, time):
        self.day = day
        self.time = time