from pynput import mouse
import time
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (time.perf_counter())))
    s = time.perf_counter()
    g = str(s)
        # Stop listener
    if not pressed:
        print(g)
        print(*f)
        return on_click
# Collect events until released
with mouse.Listener(
    on_click=on_click)as listener:
    listener.join()
