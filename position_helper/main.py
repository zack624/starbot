# -*- coding: utf-8 -*-
import numpy as np
from PIL import ImageGrab
from utils.location_finder import LocationFinder
from position import coordinate
from position_helper.visualize_areas import Visualizer
from position.coordinate import Coordinate


# track current players
def test_highlight_area(n=30):
    lf = LocationFinder(hwnd=None)
    content_area = x1, y1, x2, y2 = lf.get_window_area()
    top_left = (x1, y1)
    coor = Coordinate()

    for i in range(n):
        img = ImageGrab.grab(content_area)

        sum_list = [0] * 6
        for j in range(6):
            area = coor.get_player_highlight_areas(convert=False)[j]
            part_img = img.crop(area)
            sum_ = np.array(part_img).sum()
            sum_list[j] = sum_

        assert sum_list.count(0) >= 5
        if sum_list.count(0) == 5:
            print(sum_list.index(max(sum_list)))

        vis = Visualizer(img=img)
        vis.select_and_show_areas(coor.get_player_highlight_areas(convert=False))


def test_hand_number_area(n=10):
    lf = LocationFinder(hwnd=None)
    content_area = x1, y1, x2, y2 = lf.get_window_area()
    top_left = (x1, y1)
    coor = Coordinate()

    count = 0
    while count < n:
        img = ImageGrab.grab(content_area)
        area = coor.get_hand_number_area()[0]
        part_img = img.crop(area)
        sum_ = np.array(part_img).sum()
        if sum_ == 0:
            count += 1
            print(count)
            vis = Visualizer(img=img)
            vis.select_and_show_areas(area)


def main():
    # test_highlight_area()
    test_hand_number_area()




if __name__ == '__main__':
    main()