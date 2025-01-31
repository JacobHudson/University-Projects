import time
def Countdown(n):
    while n > 0:
        print(f"t-minus: {n}")
        n -= 1
        time.sleep(1)

from threading import Thread
t = Thread(target=Countdown, args=(10,))
t.start()

while True:
    if t.is_alive():
        print("Still Running")
    else:
        print("Completed")
