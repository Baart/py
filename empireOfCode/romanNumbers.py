def roman(number):
    r = ''
    while number / 1000 >= 1:
        number = number - 1000
        r += 'M'
    while number / 500 >= 1:
        if number >= 900:
            number -= 900
            r += 'CM'
        else:
            number = number - 500
            r += 'D'
    while number / 100 >= 1:
        if(number / 100 >= 4):
            number = number - 400
            r += 'CD'
        else:
            number = number - 100
            r += 'C'

    if number >= 90:
        number -= 90
        r+= 'XC'

    while number / 50 >= 1:
        number = number - 50
        r += 'L'

    if number >= 40:
        number = number - 40
        r += 'XL'


    while number / 10 >= 1:
        number = number - 10
        r += 'X'
    while number / 5 >= 1:
        if number == 9:
            number = number - 9
            r += 'IX'
        else:
            number = number - 5
            r += 'V'
    while number > 0:
        if number == 4:
            r += 'IV'
            number -= 4
        else:
            number = number - 1
            r += 'I'
    print r
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(4) == 'IV', '4'
    assert roman(9) == 'IX', '4'
    assert roman(88) == 'LXXXVIII', '88'
    assert roman(800) == 'DCCC', '800'
    assert roman(99) == 'XCIX', '99'
    assert roman(999) == 'CMXCIX', '999'
    assert roman(400) == 'CD', '400'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(44) == 'XLIV', '44'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert roman(3999) == 'MMMCMXCIX', '3999'
    print("Earn cool rewards by using the 'Check' button!")
