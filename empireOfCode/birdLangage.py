VOWELS = "aeiouy"


def translate(phrase):
    final = ""
    skipping = 0
    for letter in phrase:
        if skipping:
            skipping -= 1
            continue
        if letter == " ":
            pass
        elif letter in VOWELS:
            skipping = 2
        else:
            skipping = 1
        final += letter
    return final


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
