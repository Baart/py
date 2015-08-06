
import pyautogui, sys, time
print('Program started.')


# Note where the bot's window is.
#input('Move mouse over bot window and press Enter.')
#print pyautogui.position()


# locate the game window


arr = []
def init():
    for y in range(0,7):
        line = []
        for x in range(0,8):
            line.append(' ')
        arr.append(line)

def display():
    for line in arr:
        print line


def locateItems(item):
    windows = pyautogui.locateAllOnScreen(item)
    arr = []
    for win in windows:
        l = win[0]
        t = win[1]
        w = win[2]
        h = win[3]
        #pyautogui.moveTo(l+w/2, t+h/2)
        obj = {
            'x': int((l+w/2 - origin['x'])),
            'y': int((t+h/2 - origin['y']))
        }

        obj['x'] = int(obj['x'] / 87.5)
        obj['y'] = int(obj['y'] / 87.5)

        #print obj
        arr.append(obj)

    return arr

def locateWeb():
    window = pyautogui.locateOnScreen('web.png')
    l = window[0]
    t = window[1]
    w = window[2]
    h = window[3]
    #pyautogui.moveTo(l+150, t-25)
    origin = {'x': l+150, 'y': t-25}
    return origin



# 1195 1275 width item: 80px
# 1892 w total 700px

# 640 soit 60px de marge entre chaque item soit 7.5 par item

# 87.5 par item

#


    print item, " ",


def create_tab():
    items = ['fire.png', 'sword.png', 'key.png', 'wood.png', 'xshield.png', 'backpack.png', 'rock.png']
    #items = ['key.png']
    for item in items:
        print item, " ",
        items = locateItems(item)

        for itemIndex in items:

            print ".",
            #print item,  itemIndex
            #print itemIndex['y'], itemIndex['x']
            arr[itemIndex['y']][itemIndex['x']] = item[0]
        print ' '


def match(x,y, newX, newY):

    if(newX < 0 or newX >= len(arr)):
        #print "skip X", newX
        return False
    if(newY < 0 or newY >= len(arr[0])):
        #print "skip Y", newY
        return False


    if arr[x][y] == arr[newX][newY]:
        print 'found pair',y, x, " with ", newY, newX
        return True
    return False

def evaluate_case(x, y):
    value = arr[x][y]
    #print value

    for vx in [-2, -1,1, 2]:
        newX = x + vx
        match(x,y,newX, y)

    for vy in [-2, -1,1, 2]:
        newY = y + vy
        match(x,y,x, newY)


def find_pair(item):
    for idxX, line in enumerate(arr):
        for idxY, elem in enumerate(line):
            evaluate_case(idxX, idxY)
            pass
            #print idxX, idxY


#init()
#origin = locateWeb();
#create_tab()

def fake_init():
    arr.append(['f', 's', 'k', 'w', 'x', 'k', 'f', 'k'])
    arr.append(['k', 'f', 'w', 's', 'f', 'x', 's', 'f'])
    arr.append(['x', 's', 'b', 'k', 'r', 's', 'x', 'k'])
    arr.append(['w', 'r', 's', 'f', 'x', 'w', 'f', 'b'])
    arr.append(['b', 'k', 'r', 's', 'k', 's', 'r', 'k'])
    arr.append(['w', 's', 'b', 'k', 'x', 'f', 'w', 's'])
    arr.append(['k', 'f', 's', 'f', 's', 'k', 'b', 'f'])


def fake_init2():
    arr.append(['f', 'f'])
    arr.append(['k', 'f'])

fake_init()
display()

find_pair(' ')

def test():
    i = 0
    while i < 5:
        i = i + 1
        print pyautogui.position()
        #window = pyautogui.locateCenterOnScreen('wood.png')
        windows = pyautogui.locateAllOnScreen('key.png')
        #if window is None:
        #    sys.exit('Could not find game on screen. Is the game visible?')
        for window in windows:
            l = window[0]
            t = window[1]
            w = window[2]
            h = window[3]
            time.sleep(0.1)
            pyautogui.moveTo(l+w/2, t+h/2)

            #print window
            #print('Found game window at:', winLeft, winTop)
            #pyautogui.moveTo(winLeft, winTop)
            #pyautogui.click()
            #time.sleep(0.1)
            #pyautogui.click(winLeft+width, winTop+height) # click on Play button
            # navigate through start screen
            #pyautogui.click(320 + winLeft, 200 + winTop) # click on Play button
            #pyautogui.click(300 + winLeft, 380 + winTop) # click on Continue button
            #pyautogui.click(550 + winLeft, 450 + winTop) # click on Skip
            #pyautogui.click(300 + winLeft, 380 + winTop) # click on Continue button
            #pyautogui.click(botWindow) # click back on bot window
