# -*- coding: utf-8 -*-
import win32gui


class WindowFinder:

    def __init__(self, table_class=None):
        self.table_class = table_class or "PokerStarsTableFrameClass"

    def find_window_hwnd(self):
        name_text_hwnd_dict = {}

        def my_callback(hwnd, dictionary):
            name = win32gui.GetClassName(hwnd)
            text = win32gui.GetWindowText(hwnd)
            dictionary[name] = (text, hwnd)

        win32gui.EnumWindows(my_callback, name_text_hwnd_dict)
        text, hwnd = name_text_hwnd_dict[self.table_class]
        print("Window Class: ", text)
        return hwnd


def main():
    WindowFinder(table_class=None).find_window_hwnd()


if __name__ == '__main__':
    main()
