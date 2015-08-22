def common_words(first, second):
    arrFinal = []
    for w1 in first.split(','):
        print w1, second.count(',')
        if ","+w1 in second or w1+"," in second or (w1 in second and  second.count(',') == 0):
            arrFinal.append(w1)
    print arrFinal
    return ','.join(sorted(arrFinal))

def common_words2(first, second):
    return ','.join(sorted([x for x in first.split(',') if ","+x in second or x+"," in second or (x in second and second.count(',') == 0)]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    #assert common_words("one,two,three", "four,five,six") == "", "Too different"
    #assert common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    #assert common_words("mega,cloud,two,website,final", "window,penguin,literature,network,fun,cloud,final,sausage")
    assert common_words("blubber,hammer", "hammer")

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
