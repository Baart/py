

def xo_referee(game_result):

    winX = winO = 0

    # Horizontal
    for line in game_result:
        if "XXX" in line:
            winX += 1
        if "OOO" in line:
            winO += 1

    size = len(game_result)

    # Vertical

    for y in range(size):
        line = ""
        for x in range(size):
            line += game_result[x][y]
        if "XXX" in line:
            winX += 1
        if "OOO" in line:
            winO += 1

    # Diagonals
    for x in range(size):
        if(x + size) > 3:
            continue
        if(game_result[x][x] == game_result[x+1][x+1] == game_result[x+2][x+2]):
            if game_result[x][x] == "X": winX += 1
            if game_result[x][x] == "O": winO += 1

        if(game_result[x][size-1] == game_result[x+1][size-2] == game_result[x+2][size-3]):
            if game_result[x][size-1] == "X": winX += 1
            if game_result[x][size-1] == "O": winO += 1

    #print "X", winX, "O", winO
    if winX and winO: return "D"
    if winX: return "X"
    if winO: return "O"
    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert xo_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xo_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xo_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xo_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    ## Rank 2
    assert xo_referee([
        ".OX",
        ".OX",
        ".OX"]) == "D", "Mexican Vertical Duel"
    assert xo_referee([
        '.XO',
        'XXX',
        'OOO']) == "D", "Mexican Horizontal Duel"

    ## Rank 3
    assert xo_referee([
        'XOO.',
        '.X.O',
        'X.OO',
        'XXOX']) == "D", "4WD"
    assert xo_referee([
        'XOO.',
        '.X.O',
        'XXOO',
        'XXOX']) == "X", "4X4"
    print("Earn cool rewards by using the 'Check' button!")
