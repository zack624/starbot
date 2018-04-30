# -*- coding: utf-8 -*-
import numpy as np
from utils.location_finder import LocationFinder
from utils.image_matcher import ImageMatcher
from position.coordinate import Coordinate
from PIL import ImageGrab


class Monitor:

    def __init__(self, coordinate):
        self.coordinate = coordinate or Coordinate()
        self.screen_image = None
        self.image_matcher = ImageMatcher()

    def _next_screen(self):
        raise NotImplementedError

    def monitor_n_games(self, n):
        for i in range(n):
            self.monitor_one_game()

    def monitor_one_game(self):
        self.monitor_before_any_action()
        print("Acting ...")
        from position_helper.visualize_areas import Visualizer
        vs = Visualizer(img=self.screen_image)
        vs.select_and_show_areas(areas=None)
        # self.monitor_actions()

    # handle dealer position, SB/BB position, BLINDS before first player acts
    def monitor_before_any_action(self):
        self.loop_until_game_start()
        print("Game starts...")
        players = self.find_players()
        dealer_position = self.find_dealer()
        print("D: ", dealer_position)
        # todo SB/BB, BLINDS

    def loop_until_game_start(self):
        # hand_number change and pixel_sum > 0
        area = self.coordinate.get_hand_number_area()[0]

        self._next_screen()
        hand_number_image = self.screen_image.crop(area)
        new_pixel_sum = pixel_sum = np.array(hand_number_image).sum()
        while new_pixel_sum == pixel_sum:
            # print(new_pixel_sum)
            self._next_screen()
            hand_number_image = self.screen_image.crop(area)
            new_pixel_sum = np.array(hand_number_image).sum()

        while new_pixel_sum == 0:
            self._next_screen()
            hand_number_image = self.screen_image.crop(area)
            new_pixel_sum = np.array(hand_number_image).sum()

    def find_players(self):
        split_line_areas = self.coordinate.get_split_line_areas()
        split_line_images = [self.screen_image.crop(area) for area in split_line_areas]
        split_line_arrays = [np.array(image) for image in split_line_images]
        # if channel0 pixel > 228, then players are found
        channel_0_pixel_sums = [array[0].sum() for array in split_line_arrays]
        return [x > 200 * 20 for x in channel_0_pixel_sums]

    # return seat no of dealer
    def find_dealer(self):
        dealer_position = None
        dealer_areas = self.coordinate.get_dealer_areas()

        # from position_helper.visualize_areas import Visualizer
        # vs = Visualizer(self.screen_image)
        # vs.select_and_show_areas(dealer_areas)

        from PIL import Image
        dealer_array = np.array(Image.open("./background/dealer.png"))
        sum_ = None
        mini = 999999
        for i in range(510, 620):
            for j in range(200, 280):
                part_img = self.screen_image.crop((i, j, i + 24, j + 24))
                sum_ = (np.array(part_img) - dealer_array).sum()
                if mini > sum_:
                    mini = sum_
                if sum_ == 0:
                    print(i, j)
                    return
        print(mini)
        return
        while dealer_position is None:
            self._next_screen()
            images = [self.screen_image.crop(area) for area in dealer_areas]
            arrays = [np.array(image) for image in images]
            dealer_position = self.image_matcher.match_dealer(arrays)
        print(dealer_position)
        return dealer_position

    def monitor_actions(self):
        # while game not end, todo
        next_action = "player_action"
        if next_action == "player_action":
            self.monitor_player_action()
        elif next_action == "chance_action":
            self.monitor_chance_action()

    def monitor_player_action(self):
        pass

    def monitor_chance_action(self):
        pass


class ScreenMonitor(Monitor):

    def __init__(self, lf=None, coordinate=None):
        super().__init__(coordinate)
        self.location_finder = lf or LocationFinder(hwnd=None)
        self.screen_area = self.location_finder.get_window_area()

    def _next_screen(self):
        self.screen_image = ImageGrab.grab(self.screen_area)


class ReplayMonitor(Monitor):

    def __init__(self, lf=None, coordinate=None):
        super().__init__(coordinate)
        self.location_finder = lf or LocationFinder(hwnd=None)
        self.screen_area = self.location_finder.get_window_area()

    def _next_screen(self):
        self.screen_image = ImageGrab.grab(self.screen_area)

    def monitor_before_any_action(self):
        self._next_screen()
        # find players
        players = self.find_players()
        print(players)

        dealer_position = self.find_dealer()
        print("D", dealer_position)


def main():
    screen_monitor = ScreenMonitor(lf=None, coordinate=None)
    screen_monitor.monitor_n_games(10)

if __name__ == '__main__':
    main()

