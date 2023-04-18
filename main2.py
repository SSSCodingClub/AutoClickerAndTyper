import time
import threading
import os
from pygame import mixer
from pynput import keyboard

TEXT_PATH = "texts/"
delay = 0.025

keys = {eval(f"keyboard.Key.f{i+1}"): "" for i in range(12)}
texts = []
for root, dirs, files in os.walk(TEXT_PATH):
    for i,x in enumerate(zip(files, keys)):
        file, key = x
        with open(os.path.join(TEXT_PATH, file), 'r') as f:
            keys[key] = f.read()
   

mixer.init()
mixer.music.load("typing.mp3")
mixer.music.set_volume(0.5)


stopped = False

def type_text(text):
    global stopped
    mixer.music.play(-1)
    k = keyboard.Controller()
    for char in text:
        if char == "\n":
            char = keyboard.Key.enter
        # elif char == " ":
        #     char = keyboard.Key.space
        k.press(char)
        time.sleep(delay)
        k.release(char)
        if stopped:
            break
    mixer.music.stop()
        

def on_press(key):
    global stopped
    if key in keys:
        stopped = False
        t = threading.Thread(target = type_text, args = [keys[key]])
        t.start()
    elif key == keyboard.Key.pause:
        stopped = True
    elif key == keyboard.Key.esc:
        listener.stop()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()