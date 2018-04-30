# -*- coding: utf-8 -*-
from utils.window_finder import WindowFinder
import win32gui


class LocationFinder:

    def __init__(self, hwnd=None):
        self.hwnd = hwnd or WindowFinder(table_class=None).find_window_hwnd()
        self.window_area = x1, y1, x2, y2 = win32gui.GetWindowRect(self.hwnd)
        self.top_left = (x1, y1)
        self.width = x2 - x1
        self.height = y2 - y1
        self.size = (self.width, self.height)
        print("Top Left: %r, Width :%d, Height: %d" % (self.top_left, self.width, self.height))

    def get_window_area(self):
        return self.window_area

    def get_top_left(self):
        return self.top_left

    def get_size(self):
        return self.size


def main():
    LocationFinder()

if __name__ == '__main__':
    main()
