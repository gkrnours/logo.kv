import re
import numbers
from math import sin, cos, radians
import exceptions
from kivy.app import App
from kivy.uix.widget import Widget

class Turtle(Widget):
    """A turtle that can be moved on the display"""
    _self = None

    @classmethod
    def get_turtle(cls):
        return cls._self

    def __init__(self, **kw):
        if Turtle._self:
            raise(exceptions.Exception())
        Turtle._self = self
        super(Turtle, self).__init__(**kw)
        self.movements = []
        self.mov = [(0,0)]

    def _update_pos(self):
        self.movements.append(self.mov)
        self.mov = [self.relative_pos]

    def _setx(self, x):
        self.x = self.parent.center_x + float(x)

    def _sety(self, y):
        self.y = self.parent.center_y + float(y)

    def _move(self, d, r=0):
        theta = radians(r)
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
        self._move(d, self.r)

    def bk(self, d):
        """move backward by a delta d
        alias: backward"""
        self._move(d, self.r+180)
