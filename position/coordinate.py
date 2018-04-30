# -*- coding: utf-8 -*-


# get raw coordinate or transformed coordinate
class Coordinate:

    def __init__(self):
        self.hand_number_area = [(165, 74, 275, 88)]
        self.player_highlight_areas = [(800, 715), (36, 561), (36, 273), (800, 163), (1298, 273), (1298, 561)]
        self.player_highlight_w, self.player_highlight_h = 5, 5
        self.dealer_areas = [(770, 597), (335, 537), (294, 317), (559, 229), (1035, 326), (979, 537)]
        self.dealer_w, self.dealer_h = 24, 24
        self.split_line_areas = [(690, 720, 710, 721), (130, 560, 150, 561), (130, 273, 150, 274),
                                 (624, 163, 644, 164), (1189, 273, 1209, 274), (1189, 560, 1209, 561)]

    def get_player_highlight_areas(self):
        return [
            (x1, y1, x1 + self.player_highlight_w, y1 + self.player_highlight_h)
            for x1, y1 in self.player_highlight_areas]

    def get_hand_number_area(self):
        return self.hand_number_area

    def get_dealer_areas(self):
        return [(x1, y1, x1 + self.dealer_w, y1 + self.dealer_h) for x1, y1 in self.dealer_areas]

    def get_split_line_areas(self):
        return self.split_line_areas



