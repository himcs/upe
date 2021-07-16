import win32api
import win32con
from keymap import keymaps

keys = keymaps.keys()


def press(note):
    if note in keys:
        key = keymaps[note]
        win32api.keybd_event(key, 0, 0, 0)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
    return
