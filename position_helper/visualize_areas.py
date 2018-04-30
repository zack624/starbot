# -*- coding: utf-8 -*-
import cv2
import numpy as np


class Visualizer:

    def __init__(self, img):
        self.img = img

    def select_and_show_areas(self, areas):
        img_arr = np.array(self.img)
        if isinstance(areas, (tuple, )):
            area = areas
            x1, y1, x2, y2 = area
            cv2.rectangle(img_arr, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.imshow("whole", img_arr)
            cv2.waitKey(0)
        elif isinstance(areas, (list, )):
            for area in areas:
                x1, y1, x2, y2 = area
                cv2.rectangle(img_arr, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.imshow("whole", img_arr)
            cv2.waitKey(0)
        elif areas is None:
            cv2.imshow("whole", img_arr)
            cv2.waitKey(0)
        else:
            raise NotImplementedError
