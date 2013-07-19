import datetime, os, sys, unittest

"""
Used this to get the Tests to run.
The script (python) is looking for a package (Directory) called 'Domain'
"""
lib_path = os.path.abspath('../../../pyAlarm')
sys.path.append(lib_path)

from Domain.Source.pyAlarmAlarm import Alarm
from Domain.Source.pyAlarmAlarmDay import AlarmDay

class pyAlarmAlarmTest(unittest.TestCase):
    """description of class"""

    def setUp(self):
        pass

    def test_CreateAlarm(self):
        alarmTime = datetime.time(5, 0, 0)

        alarm = Alarm("Work", "Monday", "elixir", 5, False, alarmTime, True)

        self.assertEqual(False, alarm.isRepeatable, "Success")

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(pyAlarmAlarmTest)
    unittest.TextTestRunner(verbosity=2).run(suite)