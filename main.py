import inputs
import math
import threading

class XboxOneController:
    # Constants for maximum values of triggers and joysticks
    # The joystick and triggers will give integers between 0 and 255 for triggers
    # and -32768 to 32767 for joysticks, so we will normalize them to 0-1 range
    # with these constants
    max_trig_val = 256  # 2 to the power of 8, as the trigger values are unsigned 8-bit integers
    max_joy_val = 32768  # 2 to the power of 15, as the joystick values are signed 16-bit integers

    def __init__(self):
        self.left_joystick = [0, 0]
        self.right_joystick = [0, 0]
        self.left_trig = 0
        self.right_trig = 0
        self.left_bumper = 0
        self.right_bumper = 0
        self.a_button = 0
        self.x_button = 0
        self.y_button = 0
        self.b_button = 0
        self.left_joystick_button = 0
        self.right_joystick_button = 0
        self.back = 0
        self.start = 0
        # d-pad on xbox one does not work with inputs library, so we will not implement it
        # it might be my issue, if it works for you please create an issue on github to let me know
        # or if you know how to fix it, create a pull request on github

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def _monitor_controller(self):
        while True:
            events = inputs.get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.left_joystick[1] = event.state / self.max_joy_val
                elif event.code == 'ABS_X':
                    self.left_joystick[0] = event.state / self.max_joy_val
                elif event.code == 'ABS_RY':
                    self.right_joystick[1] = event.state / self.max_joy_val
                elif event.code == 'ABS_RX':
                    self.right_joystick[0] = event.state / self.max_joy_val
                elif event.code == 'ABS_Z':
                    self.left_trig = event.state / self.max_trig_val
                elif event.code == 'ABS_RZ':
                    self.right_trig = event.state / self.max_trig_val
                elif event.code == 'BTN_TL':
                    self.left_bumper = event.state
                elif event.code == 'BTN_TR':
                    self.right_bumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.a_button = event.state
                elif event.code == 'BTN_NORTH':
                    self.y_button = event.state
                elif event.code == 'BTN_WEST':
                    self.x_button = event.state
                elif event.code == 'BTN_EAST':
                    self.b_button = event.state
                elif event.code == 'BTN_THUMBL':
                    self.left_joystick_button = event.state
                elif event.code == 'BTN_THUMBR':
                    self.right_joystick_button = event.state
                elif event.code == 'BTN_SELECT':
                    self.back = event.state
                elif event.code == 'BTN_START':
                    self.start = event.state

if __name__ == '__main__':
    js = XboxOneController()
    while True:
        print(js.left_joystick, js.right_joystick)