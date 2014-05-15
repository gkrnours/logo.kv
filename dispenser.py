from copy import deepcopy
from kivy.properties import OptionProperty, ObjectProperty


class DispenserBehavior(object):
    state = OptionProperty('normal', options=('normal', 'drawn'))
    card = ObjectProperty(None)
    receiver = ObjectProperty(None)
    _card = ObjectProperty(None)

    def __init__(self, **kw):
        self.register_event_type('on_draw_card')
        self.register_event_type('on_put_card')
        super(DispenserBehavior, self).__init__(**kw)

    def on_touch_down(self, touch):
        if not self.card:
            return False
        if not self.collide_point(*touch.pos):
            return False
        if self.state == 'normal':
            self.state = 'drawn'
            self._card = self.card()
            self._card.size = 128, 96
            self._card.pos = touch.x, touch.y - self._card.height
            self._card.size_hint = None, None
            self.get_root_window().add_widget(self._card)

    def on_touch_move(self, touch):
        if self.state == 'drawn':
            self._card.pos = touch.x, touch.y - self._card.height
        else:
            return False

    def on_touch_up(self, touch):
        if self.state == 'drawn':
            self._card.parent.remove_widget(self._card)
            self.state = 'normal'
            if self.receiver and self.receiver.collide_point(*touch.pos):
                self.receiver.add_widget(self._card)
                self._card.size_hint = None, 1

    def on_draw_card(self):
        pass
    def on_put_card(self):
        pass
