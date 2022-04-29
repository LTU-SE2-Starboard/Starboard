import kivy
import os
kivy.require('2.1.0') # replace with your current kivy version !

#this gets rid of the red dot of doom
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

class Starboard (App):
        def build (self):
                interface = StarboardInterface()
                
                os.makedirs(os.path.expanduser("~/.starboard/notes"), exist_ok = True)
                os.makedirs(os.path.expanduser("~/.starboard/templates"), exist_ok = True)

                self.notes = {}
                self.pages = []
        
                self.pageWidget = NotePagesWidget()
                interface.add_widget(self.pageWidget)
                interface.add_widget(NoteTitleWidget(text = "wow"))
                
                self.createNote()
                self.createNote()
                self.createNote()
                self.createNote()
                self.selectNote("New note 1")
                self.selectNote("New note 2")
                self.selectNote("New note 3")
                self.selectNote("New note 4")
                self.selectNote("New note 2")
                return interface

        def createNote (self, template = None):
                unnamedNumber = 1
                while "New note " + str(unnamedNumber) in self.notes:
                        unnamedNumber += 1
                
                name = "New note " + str(unnamedNumber)
                self.notes[name] = Note(name, template)
                print("Created new note", name)
                pass

        def selectNote (self, name):
                try:
                        index = self.pages.index(name)
                        self.pageWidget.page = index
                except:
                        self.pages.append(name)
                        self.pageWidget.add_widget(self.notes[name].getWidget())

                note = self.notes[name]

class Note:
        def __init__ (self, path, templatePath = None):
                self.widget = NoteWidget(text = "Sample text" + path)
                self.name = path
                if templatePath:
                        loadFromPath(templatePath)
                self.text = ""
                self.open = False

        def getWidget (self):
                return self.widget

        def load (self):
                pass

        def loadFromPath (self):
                pass
        
def findNotePath (name):
        return os.path.expanduser("~/.starboard/notes/", path)
        
def findTemplatePath (name):
        return os.path.expanduser("~/.starboard/templates/", path)

class NoteWidget (Widget):
        text = StringProperty(None)

class StarboardInterface (Widget):
        pass

class NotePagesWidget (PageLayout):
        pass

class NoteTitleWidget (TextInput):
        pass

if __name__ == '__main__':
        Starboard().run()
