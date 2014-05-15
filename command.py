from os import path
from copy import deepcopy
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.core.window import Window
from dispenser import DispenserBehavior

Builder.load_file(path.join(path.dirname(__file__), 'command.kv'), rulesonly=True)

class CommandCardDispenser(DispenserBehavior, Widget):
    def on_card(self, instance, card):
        self.name = card.name
        self.color = card.color

class CommandCard(Widget):
    name = "CommandCard"
    color = 0, 0, 0

class PrimitiveCard(CommandCard):
    name = "primitive"
    color = 237/360., .45, .77
    _type = "text"

class NumberCard(PrimitiveCard):
    name = "Number"
    _type = "number"

class TurtleCard(CommandCard):
    name = "Turtle"
    color = 68/360., .99, .60

class FdCard(TurtleCard):
    name = "Forward"
