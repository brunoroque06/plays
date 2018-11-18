from pynput import mouse
from pynput.keyboard import Key, Listener
from pynput.mouse import Button

from src.KeyboardEvent import KeyboardEvent
from src.MouseEvent import MouseEvent
from src.Position import Position


class InputListener(object):
    EndRoutineKey = Key.esc
    EndStringKey = Key.ctrl_l

    def __init__(self):
        self.events = []
        self.IsRoutineComplete = False

    def IsKeyEndOfRoutine(self, key: Key) -> bool:
        return key == self.EndRoutineKey

    def IsKeyEndOfString(self, key: Key) -> bool:
        return key == self.EndStringKey

    def AddKeyboardEvent(self, key: Key, pressed: bool):
        if not(self.IsKeyEndOfRoutine(key) or self.IsKeyEndOfString(key)):
            keyboardEvent = KeyboardEvent(key, pressed)
            self.events.append(keyboardEvent)

    def PressKey(self, key) -> bool:
        self.AddKeyboardEvent(key, True)

    def ReleaseKey(self, key) -> bool:
        self.AddKeyboardEvent(key, False)
        if self.IsKeyEndOfRoutine(key):
            self.IsRoutineComplete = True
            return False
        elif self.IsKeyEndOfString(key):
            return False  # Stop listener

    def MouseClick(self, x: int, y: int, button: Button, pressed) -> bool:
        mouseEvent = MouseEvent(button, Position(x, y), pressed)
        self.events.append(mouseEvent)
        if not pressed:
            return False  # Stop listener

    def ListenOneMouseClick(self):
        with mouse.Listener(on_click=self.MouseClick) as mouseListener:
            mouseListener.join()

    def ListenOneKeyPressed(self) -> bool:
        with Listener(on_press=self.PressKey, on_release=self.ReleaseKey) as keyboardListener:
            keyboardListener.join()
        return self.IsRoutineComplete