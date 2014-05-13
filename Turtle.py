__author__ = 'ludo'

import re
import numbers
from math import sin, cos, radians
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

class Comand(BoxLayout):
    def __init__(self, **kx):
        self.register_event_type('on_callback')
        super(Command, self).__init__(**kw)

    def on_callback(self, *args):
        pass

class Turtle(Widget):
    """A turtle that can be moved on the display"""

    def __init__(self, **kw):
        super(Turtle, self).__init__(**kw)
        self.movements = []
        self.mov = [(0,0)]

    def _update_pos(self):
        self.movements.append(self.mov)
        self.mov = [self.relative_pos]

    def _setx(self, x):
        if isinstance(x, numbers.Number):
            self.x = self.parent.center_x + x
        #if isinstance(x, 'str')
        if isinstance(x, basestring):
            if re.match('[+-]', x):
                self.x += float(x)
            else:
                self.x = self.parent.center_x + float(x)

    def _sety(self, y):
        if isinstance(y, numbers.Number):
            self.y = self.parent.center_y + y
        #if isinstance(y, 'str')
        if isinstance(y, basestring):
            if re.match('[+-]', y):
                self.y += float(y)
            else:
                self.y = self.parent.center_y + float(y)

    def _move(self, d, r=0):
        theta = radians(self.r + r)
        dy, dx = int(cos(theta) * float(d)), int(sin(theta) * float(d))
        self._setx(self.relative_x + dx)
        self._sety(self.relative_y + dy)

    def home(self):
        self._setx(0)
        self._sety(0)
        self.r = 0
        self._update_pos

    def seth(self, r):
        """rotate the turtle"""
        if isinstance(r, numbers.Number):
            self.r = r
        if isinstance(r, basestring):
            if re.match('[+-]', r):
                self.r += float(r)
            else:
                self.r = float(r)

    def lt(self, r):
        """rotate left
        alias: left"""
        self.r -= float(r)

    def rt(self, r):
        """rotate right
        alias: right"""
        self.r += float(r)

    def setx(self, x):
        """move the turtle without drawing along the x axis"""
        self._setx(x)
        self._update_pos()

    def sety(self, y):
        """move the turtle without drawing along the y axis"""
        self._sety(y)
        self._update_pos()

    def tp(self, x, y):
        """move the turtle without drawing
        alias: setpos, setxy"""
        self._setx(x)
        self._sety(y)
        self._update_pos()

    def fd(self, d):
        """move forward by a delta d
        alias: forward"""
        self._move(d)

    def bk(self, d):
        """move backward by a delta d
        alias: backward"""
        self._move(d, 180)

class TurtleDisplay(Widget):
    pass

class CommandBox(BoxLayout):
    pass

class AppLayout(BoxLayout):
    pass

class TurtleApp(App):
    def build(self):
        def setx(obj):
            print obj

        return AppLayout()

if __name__ == '__main__':
    TurtleApp().run()