from __future__ import print_function
import time


def main():
    arr = init(10,10)
    randomize(arr)


    for i in range(10):
        display(arr)
        cycle(arr)
        time.sleep(0.1)
        #break


def cycle(arr):
    toggles = get_toggles(arr)
    apply_toggles(arr, toggles)


def init(w,h):
    arr = []
    for x in xrange(0,h):
        line = []
        for y in xrange(0,w):
            line.append(0)
        arr.append(line)
    return arr


def display(arr):
    print('\n\n\n\n\n')
    for line in arr:
        for char in line:
            if char == 1:
                print(' O ',end="")
            else:
                print(' . ', end="")
        print('.')


def randomize(arr):
    arr[3][2] = 1;
    arr[4][5] = 1;

    arr[3][3] = 1;
    arr[3][4] = 1;
    arr[4][3] = 1;
    arr[4][4] = 1;


def count(arr, x, y):
    count = 0
    for modx in xrange(-1,2,1):
        for mody in xrange(-1,2,1):
            if modx == 0 and mody == 0:
                continue
            #print('x:', x + modx,'  y:',  y + mody)
            count = count + arr[x + modx][y + mody]
    return count


def get_case_state(arr, x,y):

    if x == 0 or x >= len(arr[0]) -1: # out of bounds
        #print ('x out of bound', x, limit_x)
        return arr[x][y]
    if y == 0 or y >= len(arr) -1: # out of bounds
        #print ('y out of bound', y, limit_y)
        return arr[x][y]

    toggles = []
    alives = count(arr, x, y)
    #print('process:', x, y, '->', alives)
    if arr[x][y] == 1:
        if alives == 2 or alives == 3:
            return 1
    elif arr[x][y] == 0:
        if alives == 3:
            return 1
    return 0




def get_toggles(arr):
    toggles = []
    for idxY, line in enumerate(arr):
        for idxX, v in enumerate(line):
            if get_case_state(arr, idxX, idxY) != arr[idxX][idxY]:
                #print('change ->', idxX, idxY) # state, arr[idxX][idxY])
                toggles.append({"x": idxX, "y": idxY})
    return toggles

def apply_toggles(arr, toggles):
    for toggle in toggles:
        #print ('apply:', toggle['x'], toggle['y'])
        x,y = toggle['x'], toggle['y']
        if(arr[x][y] == 1):
            arr[x][y] = 0
        else:
            arr[x][y] = 1


if __name__ == '__main__':
    main();

