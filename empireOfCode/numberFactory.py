def reconstruct(n):

    print "Using ", n

    divider = 0
    arr = []
    for i in range(9,2,-1):
        if n%i == 0:
            divider1 = i
            print "divider1", divider1, n

            divider2 = int(n / float(divider1))
            print "divider2", divider2
            arr.append(divider1)
            arr.append(divider2)
            break;
    arr = list(sorted(arr))

    if len(arr) == 0:
        return 0

    result = ''

    for l in arr:
        if l >= 10:
            l = reconstruct(l)
            if l == 0:
                return 0
        result = result + str(l)

    result = ''.join(sorted(result))
    print 'r', result
    result = int(result)

    print "output", arr, result
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reconstruct(20) == 45, "1st example"
    assert reconstruct(21) == 37, "2nd example"
    assert reconstruct(17) == 0, "3rd example"
    assert reconstruct(33) == 0, "4th example"
    assert reconstruct(3125) == 55555, "5th example"
    assert reconstruct(9973) == 0, "6th example"
    assert reconstruct(560) == 2578, "6th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
