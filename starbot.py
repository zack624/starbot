# -*- coding: utf-8 -*-
from screen_monitor.monitor import ScreenMonitor, ReplayMonitor


class StarBot:

    def __init__(self):
        self.sm = ScreenMonitor(lf=None, coordinate=None)
        self.rm = ReplayMonitor(lf=None, coordinate=None)

    def play(self, n):
        self.sm.monitor_n_games(n)

    def replay(self, n):
        self.rm.monitor_n_games(n)


def main():
    sb = StarBot()
    # sb.play(10)
    sb.replay(1)


if __name__ == '__main__':
    main()
