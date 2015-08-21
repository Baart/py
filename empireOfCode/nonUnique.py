def non_unique(data):

    newData = []
    for idx, elem in enumerate(data):

        try:
            int(elem)
            if data.count(elem) > 1:
                newData.append(elem)
        except:
            count = 0
            if elem.isupper():
                count += data.count(elem)
                count += data.count(elem.lower())
            else:
                count += data.count(elem)
                count += data.count(elem.upper())

            if count > 1:
                newData.append(elem)

    return newData
    #data = [x for x in data if data.count(x) != 1]
    #return data


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    #assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

    # Rank 2
    assert non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                       'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                       'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A', 'P', 'A', 'j', 'p', 7], "Letters"

    print("All done? Earn rewards by using the 'Check' button!")