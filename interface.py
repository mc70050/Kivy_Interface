#!/usr/local/bin/python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

class MainInterface(BoxLayout):
    manager = ObjectProperty(None)

class Manager(ScreenManager):
    func1Screen = ObjectProperty(None)
    func2Screen = ObjectProperty(None)

class FunctionBar(Widget):
    pass

class F1Screen(Screen):
    pass

class F2Screen(Screen):
    pass

class InterfaceApp(App):
    def build(self):
        return MainInterface()

if __name__ == '__main__':
    InterfaceApp().run()
