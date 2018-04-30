# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np


class ImageMatcher:

    def __init__(self, mode="play"):
        if mode == "play":
            self.dealer_image = Image.open("./background/dealer.png")
            self.dealer_array = np.array(self.dealer_image)
        elif mode == "replay":
            self.dealer_image = Image.open("./background/dealer_.png")
            self.dealer_array = np.array(self.dealer_image)
        else:
            raise Exception

    # @param images list of numpy array, each array for one image
    def match_dealer(self, images):
        diff_sum = [(self.dealer_array - image).sum() for image in images]
        # print(diff_sum)
        return diff_sum.index(0) if diff_sum.count(0) == 1 else None


