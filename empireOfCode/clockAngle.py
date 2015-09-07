import math

def clock_angle(time):

    h, m = time.split(':')
    h, m = float(h), float(m)
    print h, m

    angleHeureMinute = 1/12. * m/60. * 360
    print "angleHeureMinute", angleHeureMinute

    angleHeure = h * 30.
    print "angleHeure", angleHeure

    angleHeureFinal = angleHeure + angleHeureMinute
    print "angleHeureFinal", angleHeureFinal


    angleMinute = m / 60. * 360.
    print "angleMinute", angleMinute

    r1 = (angleMinute - angleHeureFinal + 360) % 360
    r2 = angleHeureFinal%360 + 360 - angleMinute


    print "r1", r1
    print "r2", r2
    r = min(r1,r2)
    print "r", r
    if math.fabs(r - int(r)) < 0.0001:
        r = int(r)
        print "new r", r
    if r > 180:
        r = 360 - r
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
    assert clock_angle("23:59") == 5.5, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
