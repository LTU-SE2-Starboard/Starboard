import kivy
import os
kivy.require('2.1.0') # replace with your current kivy version !

#this gets rid of the red dot of doom
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

class Starboard (App):
        def build (self):
                pass

class Note:
        def __init__ (path, templatePath = None):
                name = path
                if templatePath:
                        loadFromPath(templatePath)
                text = ""
                open = False

        def getWidget ():
                return widget

        def load ():
                pass

        def loadFromPath ():
                pass
        

if __name__ == '__main__':
        os.makedirs(os.path.expanduser("~/.starboard/notes"), exist_ok = True)
        os.makedirs(os.path.expanduser("~/.starboard/templates"), exist_ok = True)
        Starboard().run()
