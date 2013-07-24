from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput

import os, sys
print "Path: %s" % os.path
print "Current script path: %s" % os.path.dirname(os.path.abspath(__file__))

sys.path.append("C:\Projects\Kivy\Alarm\pyAlarm")

from Controller.Source.AlarmController import Alarm
from Exceptions.Source.pyException import *

class CreateScreen(GridLayout):
    """description of class"""

    lblAlarmName = Label(text="Alarm Name: ")
    txtAlarmName = TextInput()

    lblSave = Label()
    btnSave = Button(text="Save")

    def callback(self, instance):
        self.CreateAlarm()
        self.lblSave.text = "Thanks! Alarm name is {0}".format(self.txtAlarmName.text)

    def __init__(self, **kwargs):        

        super(CreateScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row_force_default=True
        self.row_default_height=40
        self.padding = [20, 20, 20, 20]

        self.add_widget(self.lblAlarmName)
        self.add_widget(self.txtAlarmName)

        self.add_widget(Label(text="Repeat?", halign="left"))
        self.add_widget(CheckBox())

        self.add_widget(Label(text="Day", halign="left"))
        self.add_widget(TextInput())

        self.add_widget(Label(text="Time", halign="left"))
        self.add_widget(TextInput())

        self.add_widget(Label(text="Volume", halign="left"))
        self.add_widget(Slider())

        self.btnSave.bind(on_press=self.callback)
        self.add_widget(self.lblSave)
        self.add_widget(self.btnSave)

    def CreateAlarm(self):

        alarm = Alarm()        

        try:
            alarm.NewAlarmRequest(self.txtAlarmName.text)
        except InsufficientStorageSpaceAvailableException:
            pyGlobals.IS_RUNNING = False
            logger.Log("Shutting down...", pyGlobals.ERROR_LOG_LEVEL)
        except AlarmNameInUseException:
            pass

        import datetime
        alarmTime = datetime.datetime(2013, 7, 23, 5, 0, 0)
        snoozeLength = datetime.time(0,15)
                
        alarm.SaveAlarm(self.txtAlarmName.text, "Monday", alarmTime, "If_Only", 5, snoozeLength, True, True)

class KivyAlarmAppCreate(App):

    def build(self):
        return CreateScreen()

if __name__ == "__main__":
    KivyAlarmAppCreate().run()