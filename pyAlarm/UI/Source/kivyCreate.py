from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput

import datetime, sys
sys.path.append("C:\Projects\Kivy\Alarm\pyAlarm")

from Controller.Source.AlarmController import Alarm
from Exceptions.Source.pyException import *
from Globals.Source import pyGlobals
from Logging.Source.pyAlarmLogging import KivyLogging

kivyAppInstance = ""

# initialize the logger
logger = KivyLogging(pyGlobals.DEBUG_LOG_LEVEL, pyGlobals.SCRIPT_FILE_NAME)

class CreateScreen(GridLayout):  

    lblAlarmName = Label(text="Alarm Name: ")
    txtAlarmName = TextInput(focus=True)

    lblRepeat = Label()
    chkRepeat = CheckBox(text="Repeat?")

    lblDay = Label(text="Day")
    txtDay = TextInput()

    lblHour = Label(text="Hour")
    txtHour = TextInput()

    lblMinute = Label(text="Minute")
    txtMinute = TextInput()

    sldVolume = Slider(min=0, max=100, step=5, value=50)

    btnCancel = Button(text="Cancel")
    btnSave = Button(text="Save")

    lblResults = Label()

    def on_touch_move(self, touch):        
        self.lblResults.text = "Coords - x:{0} ___ y:{1}".format(touch.x, touch.y)

    def cancelCallback(self, instance):
        kivyAppInstance.stop()

    def saveCallback(self, instance):
        if self.ValidateFields():
            self.CreateAlarm()
            self.lblResults.text = "Thanks! Alarm '{0}' has been saved.".format(self.txtAlarmName.text)

    def __init__(self, **kwargs):        

        super(CreateScreen, self).__init__(**kwargs)

        #region Setup widgets

        self.cols = 2
        self.padding = [20, 20, 20, 20]

        self.add_widget(self.lblAlarmName)
        self.add_widget(self.txtAlarmName)

        self.add_widget(self.lblRepeat)
        self.add_widget(self.chkRepeat)

        self.add_widget(self.lblDay)
        self.add_widget(self.txtDay)        

        self.add_widget(self.lblHour)
        self.add_widget(self.txtHour)

        self.add_widget(self.lblMinute)
        self.add_widget(self.txtMinute)

        self.add_widget(Label(text="Volume"))
        self.add_widget(self.sldVolume)

        self.btnCancel.bind(on_press=self.cancelCallback)
        self.btnSave.bind(on_press=self.saveCallback)
        self.add_widget(self.btnCancel)
        self.add_widget(self.btnSave)

        self.add_widget(Label(text="Results"))
        self.add_widget(self.lblResults)

        #endregion Setup widgets

    def ValidateFields(self):

        validFields = False

        if self.txtAlarmName.text == "":
            self.txtAlarmName.focus = False
            self.txtAlarmName.hint_text = "Please specify an alarm name."
        else:
            validFields = True

        logger.Log("Slider value when saving: {0}".format(self.sldVolume.value), pyGlobals.ERROR_LOG_LEVEL)
        
        return validFields            

    def CreateAlarm(self):

        alarm = Alarm()

        try:
            alarm.NewAlarmRequest(self.txtAlarmName.text)
        except InsufficientStorageSpaceAvailableException:
            pyGlobals.IS_RUNNING = False
            logger.Log("Shutting down...", pyGlobals.ERROR_LOG_LEVEL)
        except AlarmNameInUseException:
            pass

        snoozeLength = datetime.time(0,15)
           
        custHour = int(self.txtHour.text.encode('ascii', 'ignore'))
        custMinute = int(self.txtMinute.text.encode('ascii', 'ignore'))     
        
        alarmTime = datetime.datetime(datetime.datetime.now().year, 
                                      datetime.datetime.now().month, 
                                      datetime.datetime.now().day, 
                                      hour=custHour, minute=custMinute)

        alarm.SaveAlarm(self.txtAlarmName.text, 
                        self.txtDay.text,
                        alarmTime, "If_Only", self.sldVolume.value, 
                        15, self.chkRepeat.active, True)

class KivyAlarmAppCreate(App):

    def build(self):
        return CreateScreen()

if __name__ == "__main__":
    logger.Log("Max FPS: {0}".format(Config.getint('graphics', 'maxfps')), pyGlobals.ERROR_LOG_LEVEL)
    logger.Log("Fullscreen: {0}".format(Config.get('graphics', 'fullscreen')), pyGlobals.ERROR_LOG_LEVEL)
    Config.set('graphics', 'fullscreen', 'yes')
    Config.set('graphics', 'width', 100)
    Config.set('graphics', 'height', 300)

    kivyAppInstance = KivyAlarmAppCreate()
    kivyAppInstance.run()