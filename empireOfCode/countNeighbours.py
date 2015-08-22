def count_neighbours(grid, row, col):

    count = 0
    for x in range(-1,2,1):
        for y in range(-1,2,1):
            if x == 0 and y == 0:
                continue
            newX = row + x
            newY = col + y
            if newY < 0 or newY >= len(grid[row]):
                continue
            if newX < 0 or newX >= len(grid):
                continue
            print newX, newY, len(grid)
            count += grid[newX][newY]


    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    count_neighbours(((1, 0, 1, 0, 1), (0, 1, 0, 1, 0), (1, 0, 1, 0, 1), (0, 1, 0, 1, 0), (1, 0, 1, 0, 1), (0, 1, 0, 1, 0)), 5, 4)


    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
