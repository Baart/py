FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def check_letter(letter, template):
    maxsame = 0
    bestIndex = 0
    for index, l in enumerate(template):
        correspond = 0
        for a,b in zip(letter,l):
            if a == b:
                correspond += 1
        if correspond > maxsame:
            maxsame = correspond
            bestIndex = (index+1)%10
            #print 'new best', bestIndex, l
    print 'best letter', bestIndex
    return str(bestIndex)

def recognize(image):

    template = []
    for k in range(10):
        letter = ''
        for l in range(5):
            for x in range(0+k*4,4+k*4):
                letter+=FONT[l*41 + x]
        template.append(letter)
    print template


    r = ''
    letter_count = int(len(image[0])/4)
    for k in range(letter_count):
        letter = ''
        for line in image:
            for x in range(0+k*4, 4+k*4):
                if line[x] == 0: letter+='-'
                else: letter+='X'
        r += check_letter(letter, template)
    print r
    return int(r)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    assert recognize([[0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                      [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                      [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0]]) == 1034

    print("Earn cool rewards by using the 'Check' button!")
