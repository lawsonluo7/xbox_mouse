# from mouse import MouseHandler as MouseHandler
from XInput import *
import pynput
import time

if __name__ == "__main__":
    set_deadzone(DEADZONE_TRIGGER,10)

    class MouseHandler(EventHandler):
        def __init__(self, cursor,  *controllers):
            self.cursor = cursor
            super().__init__(
                *controllers,
                )

        def process_button_event(self, event):
            if event.type == EVENT_BUTTON_PRESSED and event.button == BUTTON_RIGHT_SHOULDER:
                self.cursor.click(pynput.mouse.Button.left)
            print(event.type, event.button)

        def process_stick_event(self, event):
            self.cursor.move(event.x * 30, event.y * -30)
            print(event.stick, event.x, event.y)

        def process_trigger_event(self, event):
            pass

        def process_connection_event(self, event):
            pass

    # Create the handler and set the events functions

    cursor = pynput.mouse.Controller()
    handler = MouseHandler(cursor, 0)
    thread = GamepadThread(handler)

    thread.start()
    time.sleep(10)

else:
    raise ImportError("This is not a module. Import XInput only")