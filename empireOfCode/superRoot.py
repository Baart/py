import math

def super_root(number):
    x = 1.01
    result = 81
    last = []
    diff=1.

    while math.fabs(x**x - number) > 0.001:
        if x**x - number > 0:
            x-=diff
            diff*=0.1
        elif x**x - number < 0:
            x+=diff
        #print diff, r, r**r, result, last
    #print r, number, r**r
    return x


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        print p, result, result**result
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
    assert check_result(super_root, 10000000000), "Eighty one"
    assert check_result(super_root, 9999999999), "Eighty one"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
