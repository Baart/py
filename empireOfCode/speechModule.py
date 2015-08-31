FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"


def tell_number(number):
    initial = number
    r=""
    addSpace = ""
    if number == 0:
        return "zero"

    if number < 0:
        r += "minus"
        addSpace = " "
        number = -number

    if number >= 1000:
        thousands = int(number / 1000)
        r += addSpace + tell_number(thousands) + " thousand"
        number -= thousands * 1000
        addSpace = " "

    if number >= 100:
        cents = int(number / 100)
        r += addSpace + FIRST_TEN[cents-1] + " hundred"
        number -= cents * 100
        addSpace = " "

    if number >= 20:
        tens = int(number / 10)
        r += addSpace + OTHER_TENS[tens-2]
        number -= tens * 10
        addSpace = " "

    if number >= 10:
        r += addSpace + SECOND_TEN[number-10]
        number=0

    if number:
        r += addSpace + FIRST_TEN[number-1]

    print (initial, r)
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"
    assert tell_number(10) == 'ten', "1st example"
    assert tell_number(20) == 'twenty', "1st example"
    assert tell_number(999) == 'nine hundred ninety nine', "1st example"
    assert tell_number(30) == 'thirty', "1st example"
    assert tell_number(100) == 'one hundred', "1st example"
    assert tell_number(1000) == 'one thousand', "1st example"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")
