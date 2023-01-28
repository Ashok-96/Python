import pyautogui as pg
import time
with pg.hold('winleft'):
    pg.press('r')

time.sleep(2)
pg.typewrite('diskpart')
pg.press('enter')
