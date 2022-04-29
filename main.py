import kivy
import os
kivy.require('2.1.0') # replace with your current kivy version !

#this gets rid of the red dot of doom
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

class Starboard (App):
        pages = ObjectProperty(None)

        def build (self):
                os.makedirs(os.path.expanduser("~/.starboard/notes"), exist_ok = True)
                os.makedirs(os.path.expanduser("~/.starboard/templates"), exist_ok = True)

                notes = {}
        
                root = self.root
                # self.pages.add_widget(NoteWidget(text = "Sample text"))
                pass

        def createNote (template = None):
                pass

        def selectNote (name):
                pass

class NoteWidget (Widget):
        text = StringProperty(None)

class Note:
        def __init__ (path, templatePath = None):
                self.widget = NoteWidget(text = "Sample text")
                self.name = path
                if templatePath:
                        loadFromPath(templatePath)
                self.text = ""
                self.open = False

        def getWidget ():
                return widget

        def load ():
                pass

        def loadFromPath ():
                pass
        
def findNotePath (name):
        return os.path.expanduser("~/.starboard/notes/", path)
        
def findTemplatePath (name):
        return os.path.expanduser("~/.starboard/templates/", path)

if __name__ == '__main__':
        Starboard().run()
