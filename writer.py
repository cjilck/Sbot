from pynput import mouse
from multiprocessing import Process
import sys
import time
start_time = time.perf_counter()
def on_click(x, y, button, pressed):
    i = time.perf_counter() - start_time
    f = open('script.txt','r+')
    old = f.read()
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (i)))
    s = i
    g = str(s)
    old = str(old)
    s = str(s)
    f.write(s+'\n')
        # Stop listener
    if not pressed:
        return on_click
# Collect events until released
with mouse.Listener(
    on_click=on_click)as listener:
    listener.join()
