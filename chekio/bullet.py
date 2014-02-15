def checkio(data):

    x1, y1 = data[0]
    x2, y2 = data[1]
    x3, y3 = data[2]
    x4, y4 = data[3]



    return ((x1 - x2)*(y3-y4) - (y1 - y2)*(x3-x4) == 0)

    #replace this for solution
    return True or False

#Some hints
#You can search intersection point for lines
#Or look to rays geometry


checkio([[0,0], [0,2], [5,1], [3,1]])
checkio([[0, 0], [0, 2], [3, 1], [5, 1]])
checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) 
checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) 
checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) 
checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) 
