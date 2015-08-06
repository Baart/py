
import pyautogui, sys, time
print('Program started.')


# Note where the bot's window is.
#input('Move mouse over bot window and press Enter.')
#print pyautogui.position()


# locate the game window

while 1:

    #time.sleep(0.1)
    print pyautogui.position()
    window = pyautogui.locateOnScreen('window_reduce.png')

    if window is None:
        pass

    sys.exit('Could not find game on screen. Is the game visible?')

    winLeft = window[0]
    winTop = window[1]
    width = window[2]
    height = window[3]

    #print window

    print('Found game window at:', winLeft, winTop)

    pyautogui.moveTo(winLeft+width/2, winTop+height/2)
    #pyautogui.click()
    #time.sleep(0.1)

    #pyautogui.click(winLeft+width, winTop+height) # click on Play button


    # navigate through start screen
    #pyautogui.click(320 + winLeft, 200 + winTop) # click on Play button
    #pyautogui.click(300 + winLeft, 380 + winTop) # click on Continue button
    #pyautogui.click(550 + winLeft, 450 + winTop) # click on Skip
    #pyautogui.click(300 + winLeft, 380 + winTop) # click on Continue button
    #pyautogui.click(botWindow) # click back on bot window
