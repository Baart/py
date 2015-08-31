def safe_pawns(pawns):

    array = []
    for x in range(8):
        array.append(['_', '_', '_', '_', '_', '_', '_', '_'])

    for line in array:
        print line

    for pawn in pawns:
        x = ord(pawn[0]) - 97
        y = int(pawn[1]) - 1
        array[x][y] = "u"

    safe = 0
    for y in range(8):
        for x in range(8):
            if array[x][y] != "u": continue
            if(x > 0 and y > 0 and array[x-1][y-1] == "u"):
                safe += 1
                continue
            if(x < 7 and y > 0 and array[x+1][y-1] == "u"):
                safe += 1
                continue
    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    #assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"e8"}) == 0

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
