from pynput.keyboard import Key, Controller
import pygetwindow as gw
import subprocess
import time

keyboard = Controller()

def startLoop():
    ii = 0
    fruits = ["apple", "banana", "cherry"]

    for i in range(50):

        for x in fruits:
            subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')                 

            time.sleep(1.2)
            ii += 7 - 2 * 3 + i + 2

            bot(str(ii) + " fruits that beat " + x)
            time.sleep(1.2)

def bot(message):
    keyboard.type(message)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

startLoop()
