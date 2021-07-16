import threading

from presskey import press
from server import sock
from watch_dog import watch_dog, in_game

name = "原神"
threading.Thread(target=watch_dog, args=(name,)).start()
while True:
    data, addr = sock.recvfrom(1024)
    if in_game():
        press(int(data))
    else:
        print(name, "is not font")
