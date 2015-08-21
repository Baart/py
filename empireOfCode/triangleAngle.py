import math

def angles(a, b, c):

    try:
        alpha = math.acos( (b*b + c*c - a*a) / (2.*b*c))
        beta  = math.acos( (c*c + a*a - b*b) / (2.*c*a))
        gamma = math.acos( (a*a + b*b - c*c) / (2.*a*b))
    except:
        return [0,0,0]

    if alpha == 0 or beta == 0 or gamma == 0:
        return [0,0,0]

    alpha = 180 * alpha / math.pi
    beta = 180 * beta / math.pi
    gamma = 180 * gamma / math.pi


    alpha = int(round(alpha));
    beta = int(round(beta));
    gamma = int(round(gamma));

    return sorted([alpha, beta, gamma])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
