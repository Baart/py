

def swap_sort(arr):
    array = []
    for elem in arr:
        array.append(elem)
    sequence = []
    while sorted(array) != array:
        first = array[0]
        for idx, elem in enumerate(array):
            if first > elem:
                sequence.append(str(idx) + str(idx-1))
                array[idx] = first
                array[idx-1] = elem
                break
            first = elem
    return ','.join(sequence)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True

    assert check_solution(swap_sort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swap_sort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swap_sort, (1, 2, 3, 5, 3)), "One move"
