import inputs
import pynput
import time
import threading

cursor = pynput.mouse.Controller()

x = 0
y = 0

def move_mouse(cursor):
    global x
    global y
    while True:
        time.sleep(0.1)
        cursor.move(x, y)

monitor_thread = threading.Thread(target=move_mouse, args=(cursor,), daemon=True)
monitor_thread.start()

for i in range(10000):
    time.sleep(0.03)
    events = inputs.get_gamepad()
    for event in events:
        if event.code == "ABS_RX":
            x = (event.state / 32768) * 30
    
        elif event.code == "ABS_RY":
            y = (event.state / 32768) * -30

        elif event.code == "BTN_TL":
            if event.state:
                cursor.press(pynput.mouse.Button.left)
            else:
                cursor.release(pynput.mouse.Button.left)