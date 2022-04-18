import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget

class StarboardInterface (Widget):
        pass

class Starboard (App):
        def build (self):
                return StarboardInterface()


if __name__ == '__main__':
        Starboard().run()
