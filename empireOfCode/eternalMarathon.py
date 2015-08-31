def chase(a2, a1, b):

    b2 = - a2 * b
    print "a1", a1
    print "a2", a2
    print "b ", b
    print "b2", b2
    t = b2 / float(a1-a2)

    print t
    return t

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(chase(2, 1, 1), 2, 8), "example"
    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"

    print("All set? Click 'Check' to review your code and earn rewards!")
