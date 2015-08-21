def check_pangram(text):
    text = text.replace(' ', '')
    text = text.replace('.', '')
    text = text.lower()

    for x in range(97,97+26):
        #print chr(x), text.count(chr(x))
        if text.count(chr(x)) == 0:
            return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

    print("All done? Earn rewards by using the 'Check' button!")
