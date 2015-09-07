OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction": return x and y
    if operation == "disjunction": return x or y
    if operation == "implication":
        if x:
            return y
        return True
    if operation == "exclusive":   return x!=y
    if operation == "equivalence": return x==y


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "implication") == 1, "material"
    assert boolean(1, 0, "implication") == 0, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

    print("All done? Earn rewards by using the 'Check' button!")
