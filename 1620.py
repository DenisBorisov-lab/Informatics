import keyboard
from time import sleep


def keylogger(e):
    a = e.event_type
    name = e.name


keyboard.hook(keylogger)
keyboard.wait()