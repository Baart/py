import itertools

def checkio(data):

    grille, template = data[0], data[1]

    password = ""

    for i in range(4):
        for line1, line2 in zip(grille, template):
            for char1, char2 in zip(line1, line2):
                if(char1 == "X"):
                    password+=char2
        grille = list(zip(*grille[::-1]))

    print("password", password)

    return password

#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


checkio([
        ['X...',
         '..X.',
         'X..X',
         '....'],
        ['itdf',
         'gdce',
         'aton',
         'qrdi']])

checkio([
        ['....',
         'X..X',
         '.X..',
         '...X'],
        ['xhwc',
         'rsqx',
         'xqzz',
         'fyzr']])
