import pyautogui

import random
import time
#help(pyautogui)
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

#pyautogui.alert('This is an alert box.')


pyautogui.moveTo(1650, 180)

i = 0;
while i < 10:
    i = i + 1
    print i
    pyautogui.click()
    time.sleep(0.1)



#while 1:
#    randX = random.randint(0,screenWidth)
#    randY = random.randint(0,screenHeight)
#    pyautogui.moveTo(randX, randY)
#    time.sleep(1)


