import inputs
import pynput
import threading

class XboxOneController:
    # Constants for maximum values of triggers and joysticks
    _max_trig_val = 256  # 2 to the power of 8, as the trigger values are unsigned 8-bit integers
    _max_joy_val = 32768  # 2 to the power of 15, as the joystick values are signed 16-bit integers
    def __init__(self):
        self.l_joy = self._placeholder_callable
        self.r_joy = self._placeholder_callable
        self.l_trig = self._placeholder_callable
        self.r_trig = self._placeholder_callable
        self.l_bumper = self._placeholder_callable
        self.r_bumper = self._placeholder_callable
        self.a = self._placeholder_callable
        self.x = self._placeholder_callable
        self.y = self._placeholder_callable
        self.b = self._placeholder_callable
        self.l_joy_btn = self._placeholder_callable
        self.r_joy_btn = self._placeholder_callable
        self.back = self._placeholder_callable
        self.start = self._placeholder_callable
        self.dpad = self._placeholder_callable

        self._dpad_x = 0
        self._dpad_y = 0
        self._l_joy_x = 0
        self._l_joy_y = 0
        self._r_joy_x = 0
        self._r_joy_y = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.start()

    def _placeholder_callable(self, *args, **kwargs):
        pass

    def _monitor_controller(self):
        while True:
            events = inputs.get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self._l_joy_y = event.state / self._max_joy_val
                    self.l_joy(self._l_joy_x, self._l_joy_y)
                elif event.code == 'ABS_X':
                    self._l_joy_x = event.state / self._max_joy_val
                    self.l_joy(self._l_joy_x, self._l_joy_y)
                elif event.code == 'ABS_RY':
                    self._r_joy_y = event.state / self._max_joy_val
                    self.r_joy(self._r_joy_x, self._r_joy_y)
                elif event.code == 'ABS_RX':
                    self._r_joy_x = event.state / self._max_joy_val
                    self.r_joy(self._r_joy_x, self._r_joy_y)
                elif event.code == 'ABS_Z':
                    self.l_trig(bool(event.state) / self._max_trig_val)
                elif event.code == 'ABS_RZ':
                    self.r_trig(bool(event.state) / self._max_trig_val)
                elif event.code == 'BTN_TL':
                    self.l_bumper(bool(event.state))
                elif event.code == 'BTN_TR':
                    self.r_bumper(bool(event.state))
                elif event.code == 'BTN_SOUTH':
                    self.a(bool(event.state))
                elif event.code == 'BTN_NORTH':
                    self.y(bool(event.state))
                elif event.code == 'BTN_WEST':
                    self.x(bool(event.state))
                elif event.code == 'BTN_EAST':
                    self.b(bool(event.state))
                elif event.code == 'BTN_THUMBL':
                    self.l_joy_btn(bool(event.state))
                elif event.code == 'BTN_THUMBR':
                    self.r_joy_btn(bool(event.state))
                elif event.code == 'BTN_SELECT':
                    self.back(bool(event.state))
                elif event.code == 'BTN_START':
                    self.start(bool(event.state))
                elif event.code == 'ABS_HAT0X':
                    self._dpad_x = bool(event.state)
                    self.dpad(self._dpad_x, self._dpad_y)
                elif event.code == 'ABS_HAT0Y':
                    self._dpad_y = bool(event.state)
                    self.dpad(self._dpad_x, self._dpad_y)
                

if __name__ == '__main__':
    cursor = pynput.mouse.Controller()
    def on_r_joy_move(x, y):
        cursor.move(round(x, 5)**3 * 30, round(y, 5)**3 * -30)

    def on_l_bumper(pressed):
        if pressed:
            cursor.press(pynput.mouse.Button.left)
        else:
            cursor.release(pynput.mouse.Button.left)

    js = XboxOneController()

    js.l_joy = on_r_joy_move
    js.l_bumper = on_l_bumper
