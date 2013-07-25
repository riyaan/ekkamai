from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput

import sys
sys.path.append("C:\Projects\Kivy\Alarm\pyAlarm")

from Controller.Source.AlarmController import Alarm
from Exceptions.Source.pyException import *

kivyAppInstance = ""

class CreateScreen(GridLayout):
    """description of class"""    

    lblAlarmName = Label(text="Alarm Name: ")
    txtAlarmName = TextInput()

    lblRepeat = Label()
    chkRepeat = CheckBox(text="Repeat?")

    lblDay = Label(text="Day")
    txtDay = TextInput()

    sldVolume = Slider(min=0, max=100, value=25)

    btnCancel = Button(text="Cancel")
    btnSave = Button(text="Save")

    lblResults = Label()

    def on_touch_move(self, touch):
        self.lblResults.text = "Coords - x:{0} ___ y:{1}".format(touch.x, touch.y)

    def cancelCallback(self, instance):
        kivyAppInstance.stop()

    def saveCallback(self, instance):
        self.CreateAlarm()
        self.lblResults.text = "Thanks! Alarm name is {0}".format(self.txtAlarmName.text)

    def __init__(self, **kwargs):        

        super(CreateScreen, self).__init__(**kwargs)

        # region Setup widgets
        self.cols = 2
        self.row_force_default=True
        self.row_default_height=40
        self.padding = [20, 20, 20, 20]

        self.add_widget(self.lblAlarmName)
        self.add_widget(self.txtAlarmName)

        self.add_widget(self.lblRepeat)
        self.add_widget(self.chkRepeat)

        self.add_widget(self.lblDay)
        self.add_widget(self.txtDay)

        self.add_widget(Label(text="Time"))
        self.add_widget(TextInput())

        self.add_widget(Label(text="Volume"))        
        self.add_widget(self.sldVolume)

        self.btnCancel.bind(on_press=self.cancelCallback)
        self.btnSave.bind(on_press=self.saveCallback)
        self.add_widget(self.btnCancel)
        self.add_widget(self.btnSave)

        self.add_widget(self.lblResults)

        # End Setup widgets

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
    kivyAppInstance = KivyAlarmAppCreate()
    kivyAppInstance.run()