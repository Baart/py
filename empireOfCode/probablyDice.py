import itertools

def probability(dice_number, sides, target):
    print "---", dice_number, sides, target
    total = 0
    hit = 0

    total = sides**dice_number
    for x in itertools.product(range(1,sides+1),repeat=dice_number):
        if sum(x) == target:
            hit+=1
    r = hit/float(total)
    print r
    return r



def dice_frequency(sides, rolls):
    if rolls == 1:
        return [1]*sides
    prev = dice_frequency(sides, rolls-1)
    return [sum(prev[i-j] for j in range(sides) if 0 <= i-j < len(prev))
            for i in range(rolls*(sides-1)+1)]



def probability(rolls, sides, t):
    freq = dice_frequency(sides,rolls)
    freq_sum = sides**rolls
    for target in range(rolls,rolls*sides+1):
        print target
        index = target-rolls
        if 0 <= index < len(freq):
            print("%2d : %2d, %f" % (target, freq[index], freq[index]/float(freq_sum)))
        else:
            print("%2d : %2d, %f" % (target, 0, 0.0))
        if target ==t:
            print "got result"
            return round(freq[index]/float(freq_sum), 5)
    return 0


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    #assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    #assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    #assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    #assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    #assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    #assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
