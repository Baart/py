import operator

valids = []
for x in range(26):
    valids.append(chr(x+65))
    valids.append(chr(x+97))

def most_letter(text, all_letters=False):
    a = {}
    for letter in text:
        if letter not in valids:
            continue
        try :
            a[letter.lower()] += 1
        except:
            a[letter.lower()] = 1


    sorted_a = sorted(a.items(), key=operator.itemgetter(0))
    #print "etape 1", sorted_a
    sorted_a = list(reversed(sorted_a))
    #print "etape 2", sorted_a
    sorted_a = sorted(sorted_a, key=operator.itemgetter(1))
    #print "etape 3", sorted_a
    sorted_a = list(reversed(sorted_a))
    #print "etape 4", sorted_a
    r = ''.join([x[0] for x in sorted_a])

    print r

    if not all_letters:
        return r[0]

    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank_1

    assert most_letter("Hello World!") == "l", "Hello test"
    assert most_letter("How do you do?") == "o", "O is most wanted"
    result = most_letter("One")
    assert len(result) == 1 and result in "one", "All letter only once."
    assert most_letter("Oops!") == "o", "Don't forget about lower case."
    result = most_letter("AAaooo!!!!")
    assert len(result) == 1 and result in "ao", "Only letters."
    result = most_letter("abe")
    assert len(result) == 1 and result in "abe", "The First."
    result = most_letter("Lorem ipsum dolor sit amet")
    assert len(result) == 1 and result in "mo", "Lorem 1."

    # Rank_2
    assert most_letter("Lorem ipsum dolor sit amet") == "m", "Lorem 2."
    assert most_letter("One") == "e", "One 2"
    assert most_letter("AAaooo!!!!") == "a", "Only letters. 2"
    assert most_letter("bcdefghijklmnaopqrstuvwxyz") == "a", "ABC"



    # Rank_3
    assert most_letter("Lorem ipsum dolor sit amet", True) == "moeilrstadpu", "Lorem 3."


    print("Use 'Check' to earn sweet rewards!")
