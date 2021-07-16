import win32gui
import time

flag = False


def watch_dog(name):
    global flag
    while True:
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) != name:
            flag = False
        else:
            flag = True
        time.sleep(0.01)


def in_game():
    global flag
    return flag
