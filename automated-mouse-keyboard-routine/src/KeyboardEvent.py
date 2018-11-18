from pynput.keyboard import Key, Controller


class KeyboardEvent(object):
    def __init__(self, key: Key, pressed: bool) -> object:
        self.key = key
        self.pressed = pressed

    def process(self):
        keyboard = Controller()
        if self.pressed:
            keyboard.press(self.key)
        else:
            keyboard.release(self.key)
