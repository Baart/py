


print 'test'




def count_units(number):
    count = 0
    txt = str(int(bin(number)[2:]))
    print txt
    for letter in txt:
        if letter == "1":
            count += 1
    print "returning", count
    return count




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_units(4) == 1
    assert count_units(15) == 4
    assert count_units(1) == 1
    assert count_units(1022) == 9
