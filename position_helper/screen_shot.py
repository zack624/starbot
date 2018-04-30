# -*- coding: utf-8 -*-

from position.coordinate import Coordinate
from utils.location_finder import LocationFinder
from position_helper.visualize_areas import Visualizer
from PIL import ImageGrab
from PIL import Image
import numpy as np


def shot_whole_screen():
    lf = LocationFinder(hwnd=None)
    screen_area = lf.get_window_area()
    screen_image = ImageGrab.grab(screen_area)
    screen_image.save("../background/whole.png")
    return screen_image


def crop_dealer_of_p0():
    screen_image = Image.open("../background/whole.png")
    coordinate = Coordinate()
    dealer_areas = coordinate.get_dealer_areas()

    vs = Visualizer(img=screen_image)
    vs.select_and_show_areas(dealer_areas)

    p0_dealer_area = dealer_areas[0]
    p0_dealer_image = screen_image.crop(p0_dealer_area)
    p0_dealer_image.save("../background/dealer.png")


# shot_whole_screen()
# crop_dealer_of_p0()


def find_dealer_area_on_screen():
    dealer_image = Image.open("../background/dealer.png")

    lf = LocationFinder(hwnd=None)
    screen_area = lf.get_window_area()
    screen_image = ImageGrab.grab(screen_area)
    print(screen_image)

    for x in range(463):
        for y in range(386):
            part_img = screen_image.crop((x, y, x + 24, y + 24))
            diff = np.array(dealer_image) - np.array(part_img)
            diff = abs(diff)
            if diff.sum() == 0:
                print(x, y)
                vs = Visualizer(img=screen_image)
                vs.select_and_show_areas((x, y, x + 24, y + 24))
                return


# find_dealer_area_on_screen()


def get_replay_dealer():
    screen_image = Image.open("../background/whole_active.png")
    coordinate = Coordinate()
    area = coordinate.get_dealer_areas()[3]
    img = screen_image.crop(area)
    img.save("../background/dealer_.png")


get_replay_dealer()


