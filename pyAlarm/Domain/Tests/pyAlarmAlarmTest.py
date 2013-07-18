import datetime
import unittest

#from Domain.Source.pyAlarmAlarm import Alarm
#from Domain.Source.pyAlarmAlarmDay import AlarmDay

class pyAlarmAlarmTest(unittest.TestCase):
    """description of class"""

    def setUp(self):
        pass

    def test_CreateAlarm(self):

        alarmTime = datetime.time(5, 0, 0)

        alarm = Alarm("Work", "Monday", "elixir", 5, False, alarmTime, True)

        self.assertEqual(False, alarm.isRepeatable, "Success")

    if __name__ == '__main__':
        unittest.main()