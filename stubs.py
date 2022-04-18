import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

class Note:
    def __init__(path, templatePath = None):
        open = False
        name = ""
        #content = the Section kivy widget
        #widget(?)

    def getWidget()

    def saveAsTemplate()

    def insertResource(recType, path)

    def switchPath(newPath)

    def loadFromPath(path) #I don't think public and private functions exist in py

    def save()

    


class Starboard:
    def __init__():
        testNote = Note("")

        #dictionary (C++ map) for a string to a note
        notes = {"testNote": testNote}

    def build(self)

    def createNote(note = None) #the note is a template

    def hoverLink()

    def selectNote(name)
    
