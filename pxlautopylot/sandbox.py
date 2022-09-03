from pynput.mouse import Listener, Button
from win32gui import GetForegroundWindow, GetWindowText

from pxlautopylot.pixel import Pixel


def handle_click(x, y):
    window_name = GetWindowText(GetForegroundWindow())
    pixel = Pixel(x, y)
    print("{{ 'window_name': '{0}', 'pixel': {1} }}".format(window_name, pixel))


class Sandbox:

    def __init__(self, n):
        self.n = n

    def run(self):
        self._info()
        with Listener(on_click=self._on_click) as listener:
            listener.join()
            print("finished.")

    def _info(self):
        print("{0} pixels remaining to describe. Press right click to stop.".format(self.n))

    def _on_click(self, x, y, button, pressed):
        if pressed:
            return True
        if self.n < 1 or button == Button.right:
            return False
        else:
            handle_click(x, y)
            self.n -= 1
            if self.n < 1:
                return False
            else:
                self._info()

