import pyautogui
import time

time.sleep(3)

# ----------------- FIRST PART ---------------- #

# --- Check dinos top of the nose position. Run program and set mose pointer on the dinos top of the nose.

print(pyautogui.position())

# Main result: Point(x=189, y=315), so in second part I will chose x=190, y=300 as x and y of region to do screenshot.