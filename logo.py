import re
import numbers
from math import sin, cos, radians
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from turtle import Turtle

class Timeline(Widget):
    pass

class LogoApp(App):
    def build(self):
        return Factory.AppLayout()

if __name__ == '__main__':
    LogoApp().run()