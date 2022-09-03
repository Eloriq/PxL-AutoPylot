import win32gui
from pxlautopylot.color import Color


class Pixel:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_color(self):
        desktop_window_id = win32gui.GetDesktopWindow()
        desktop_window_dc = win32gui.GetWindowDC(desktop_window_id)
        long_color = win32gui.GetPixel(desktop_window_dc, self.x, self.y)
        int_color = int(long_color)
        return Color((int_color & 0xff), ((int_color >> 8) & 0xff), ((int_color >> 16) & 0xff))

    def is_darker_than(self, color: Color):
        return self.get_color().is_darker_than(color)

    def is_same_color(self, color: Color):
        return self.get_color().equals(color)

    def __str__(self):
        return "{{ 'x': {0}, 'y': {1}, 'color': {2} }}".format(self.x, self.y, self.get_color())
