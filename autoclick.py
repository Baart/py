
import win32api
import win32con
import time
import re

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


filename = "coords_clicks.txt"


def info():
    while 1:
        time.sleep(0.3)
        line = "{0}".format(win32api.GetCursorPos())
        print(line)
            
def gather():
    with open(filename, "w") as f:
        while 1:
            time.sleep(1)
            line = "{0}".format(win32api.GetCursorPos())
            print(line)
            f.write(line+"\n")
        
        
def apply():
    with open(filename, "r") as f:
        for line in f.readlines():
            coord = re.findall("\d+", line)
            x = int(coord[0])
            y = int(coord[1])
            click(x,y)
            time.sleep(0.5)
            x = 3731
            y = 812
            click(x,y)
            time.sleep(0.5)



count = 50

startx, endx = 2090, 3384
length = endx-startx
step =  int(length / count)
starty = 950
snapbtn = (3720, 1060)

        
def autosnaps():
    moved = 0
    for x in range(startx, endx, step):
        if(int((x - startx)/step) > count):
            break;
        print( str(int((x - startx)/step))+"/"+str(count))
        click(x,starty)
        time.sleep(0.9)

        if(win32api.GetCursorPos()[0] != x):
            moved += 1
            print("Moved, keep moving to stop")
            if(moved > 1):
                break;
        
        click(snapbtn[0],snapbtn[1])
        time.sleep(0.01)

autosnaps()
#apply()
#gather()
#info()
