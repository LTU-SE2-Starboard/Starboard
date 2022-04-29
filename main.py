import kivy
kivy.require('2.1.0') # replace with your current kivy version !

#this gets rid of the red dot of doom
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

class Starboard (App):
        def build(self):
                pass

if __name__ == '__main__':
        Starboard().run()
