from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

class UpdateScreen(GridLayout):
    """description of class"""

    def __init__(self, **kwargs):
        super(UpdateScreen, self).__init__(**kwargs)
        self.cols = 2

        dropDown = DropDown()
        for index in range(10):
            btn = Button(Text="Value %d" % index, size_hint_y=None, height=44)
            dropDown.add_widget(btn)

        self.add_widget(dropDown)

class KivyAlarmAppUpdate(App):

    def build(self):
        return UpdateScreen()

if __name__ == "__main__":
    KivyAlarmAppUpdate().run()