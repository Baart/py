def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}

    while stack:
        print "stack is", stack
        path, current = stack.pop()
        print "path is", path
        print "current is", current
        for k, v in current.items():
            print "k is", k
            print "v is", v
            if isinstance(v, dict):
                print "v is a dict"
                if not v:
                    print "emptyness of a value"
                    result["/".join((path + (k,)))] = ""
                else:
                    print "non emptyness"
                print "la", path + (k,)
                print "ic", v
                stack.append((path + (k,), v))
            else:
                print "v is not a dict"
                print "result", result
                result["/".join((path + (k,)))] = v
                print "result became", result
        print "stack became", stack
        print ""
    print "result", result
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({
        "name": {
            "first": "One",
            "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}, "Not Simple"
    print("All done? Earn rewards by using the 'Check' button!")
