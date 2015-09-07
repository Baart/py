import math
def spheroid(height, width):
    c = height / 2.0
    a = width / 2.0
    surface = 0.0

    volume = 4 * math.pi / 3. * a**2 * c

    if c < a: # use oblate formula
        e_square = 1 - c**2/a**2
        e = math.sqrt(e_square)
        surface = (2 * math.pi * a**2) * (1 + ((1-e_square)/e) * math.atanh(e) )

    print "volume", volume
    print "surface", surface
    return round(volume, 2), round(surface, 2)

if __name__ == '__main__':
    assert list(spheroid(2, 4)) == [16.76, 34.69]
