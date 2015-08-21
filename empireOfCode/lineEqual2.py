def check_line(line):
    last = line[0]
    for idx, elem in enumerate(line):
        if idx != 0:
            if last == elem:
                return False
        last = elem
    return True


def check_grid(grid):

    for idx, line in enumerate(grid):
        if not check_line(line):
            return False

        if idx+1 < len(grid):
            nextLine = grid[idx+1]
            if len(line) % 2 == 0 and line[len(line)-1] != nextLine[0]:
                return False

            if len(line) % 2 == 1 and line[len(line)-1] == nextLine[0]:
                return False

    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"

    print("Use 'Check' to earn sweet rewards!")
