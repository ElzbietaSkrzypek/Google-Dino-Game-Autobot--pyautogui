import pyautogui
import time
import numpy as np
from PIL import Image

time.sleep(3)

# -------------- SECOND PART ----------------- #

while True:
    image = pyautogui.screenshot("screenshot3.png", region=(
        190, 300, 120, 100))  # 120 and 100 is a weight and height of region which works for me.

    img = np.asarray(Image.open("screenshot3.png"))  # set np array to count pixels on screenshot

    black_pixel_sum = np.sum(img < 100)
    white_pixel_sum = np.sum(img > 100)
    print(black_pixel_sum)
    print(white_pixel_sum)  # - at the beginning it helps me to set the range of light and dark mode

    # light mode - black pixel sum to 30000
    if 350 < black_pixel_sum < 30000:
        pyautogui.press('up')

    # dark mode - black pixel over 30000 and white pixels over 1000 works properly for my.
    # I estimated this range by observation white and dark pixels printed.
    elif 30000 < black_pixel_sum and white_pixel_sum > 1000:
        pyautogui.press('up')
