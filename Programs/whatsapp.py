# importing the module
import subprocess
import pywhatkit as pwk
import pyautogui as pg
import webbrowser as wb
import time
wb.open('https://web.whatsapp.com/')
time.sleep(10)
for i in range(20):
    pg.typewrite('ley lawyer!!',interval='0.5')
    pg.press("Enter")
"""time.sleep(5)
pg.mouseDown(x=718, y=1055, duration=3)
pg.leftClick()
pg.typewrite('cmd')
pg.press('Enter')
time.sleep(10)
pg.typewrite('exit')
time.sleep(5)
pg.press('Enter')
time.sleep()
print(pg.position())"""


#pwk.sendwhatmsg_instantly("+919066594673",message="hello",wait_time=10,tab_close=True)