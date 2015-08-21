
import math

def simple_areas(*args):
    if len(args) == 1:
        result = args[0]/2.**2. * math.pi
        pass
    if len(args) == 2:
        result = args[0]*args[1]
        pass
    if len(args) == 3:
        a = args[0]
        b = args[1]
        c = args[2]
        s = 0.5*(a+b+c)
        result = math.sqrt( s*(s-a)*(s-b)*(s-c) )
        pass
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
