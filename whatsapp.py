# importing the module
import pywhatkit as pwk
import pyautogui as pg
import webbrowser as wb
import time
# using Exception Handling to avoid
wb.open('https://web.whatsapp.com')
time.sleep(20)
with open('./msg.txt','r') as msg:
    for i in msg:
        pg.typewrite(i)
        time.sleep(3)
        pg.press('Enter')

        

"""string=''
time.sleep(11)
for i in string:
    pg.press(i)
try:
# sending message to receiver
# using pywhatkit
    while counter < 10:
        msg="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        pwk.sendwhatmsg_to_group_instantly(Group_Name,"hello all!!",tab_close=True)
        counter+=1
except:
# handling exception
# and printing error messagello A
    print("An Unexpected Error!")
   
"""
