from XInput import *
import pynput
import time


set_deadzone(DEADZONE_LEFT_THUMB, 20)

class MyHandler(EventHandler):
    keyboard = pynput.keyboard.Controller()
    cursor = pynput.mouse.Controller()
    keybinds = {
        "LEFT_THUMB": None,
        "RIGHT_THUMB": None,
        "LEFT_SHOULDER":  pynput.mouse.Button.left,
        "RIGHT_SHOULDER": pynput.mouse.Button.right,
        "BACK": None,
        "START": None,
        "DPAD_LEFT": pynput.keyboard.Key.left,
        "DPAD_RIGHT": pynput.keyboard.Key.right,
        "DPAD_UP": pynput.keyboard.Key.up,
        "DPAD_DOWN": pynput.keyboard.Key.down,
        "A": None,
        "B": None,
        "Y": None,
        "X": None,
    }

    def process_button_event(self, event):
        button = self.keybinds.get(event.button)
        device = self.cursor if type(button) == pynput.mouse.Button else self.keyboard
        func = device.press if event.type == EVENT_BUTTON_PRESSED else device.release
        if button is not None:
            func(button)
    
    def process_stick_event(self, event):
        if event.stick == 1:
            self.cursor.move(round(event.x, 1)**3 * 20, round(event.y, 1)**3 * -20)
        elif event.stick == 0:
            self.cursor.scroll(round(event.x, 1)**3 * 2, round(event.y, 1)**3 * 2)

    def process_trigger_event(self, event):
        pass
    
    def process_connection_event(self, event):
        pass

handler = MyHandler(0)
thread = GamepadThread(handler)
thread.daemon = False
thread.start()
while True:
    time.sleep(3600)
