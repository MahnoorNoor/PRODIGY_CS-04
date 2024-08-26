# Simple Keylogger

## Project Overview

This project is a simple keylogger tool that records and logs keystrokes. The primary focus of this tool is to log the keys pressed on a keyboard and save them to a file. **Ethical considerations and permissions are crucial for projects involving keyloggers.** This tool is intended for educational purposes only and should not be used without explicit consent from the user being monitored.

## Features

- Logs all keystrokes, including both character keys and special keys (e.g., Enter, Shift).
- Saves the recorded keystrokes to a text file.
- Simple and lightweight design.

## How It Works

The keylogger utilizes the `pynput` library to listen for keyboard events. When a key is pressed, the keylogger records the key and appends it to a log file on your system.

## Installation

1. **Clone the repository:**
   ```bash
   git clonehttps://github.com/MahnoorNoor/PRODIGY_CS-04.git
   cd simple-keylogger

   Install the required dependencies:
   pip install pynput

 ## Key Components of the Code
 
 **on_press(key):**

- This function is triggered every time a key is pressed.
- The function attempts to log the character key (e.g., 'a', 'b', 'c').
- If the key is a special key (e.g., Enter, Shift), it logs the key name

 **open("filename", "a")**
- The file is opened in append mode using the "a" flag. This ensures that new keystrokes are added to the end of the file without overwriting existing data.

## Ethical Considerations
**Important:** Keylogging can be intrusive and is illegal without consent. This tool is intended for educational purposes only. Always ensure you have permission from the user whose keystrokes you intend to log.