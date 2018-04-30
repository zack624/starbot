# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
from position_helper.visualize_areas import Visualizer


image = Image.open("./background/whole_active.png")
array = np.array(image)

areas = [(690, 720, 710, 721),
         (130, 560, 150, 561), (130, 273, 150, 274),
         (624, 163, 644, 164),
         (1189, 273, 1209, 274), (1189, 560, 1209, 561)]

active_array = np.array(image.crop(areas[0]))

vs = Visualizer(img=image)
vs.select_and_show_areas(areas=areas)

# for i in range(1336):
#     for j in range(949):
#         area = (i, j, i + 20, j + 1)
#         part_img = image.crop(area)
#         diff = active_array - np.array(part_img)
#         diff_sum = diff.sum()
#         if diff_sum == 0:
#             print(i, j)






