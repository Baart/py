def cache(function):
    cached_values = {}  # Contains already computed values

    def wrapping_function(*args):
        print (hex(id(cached_values)))
        if args not in cached_values:
            # Call the function only if we haven't already done it for those parameters
            #print('caching value')
            cached_values[args] = function(*args)
        #print('cache is:', cached_values)
        return cached_values[args]
    return wrapping_function

@cache
def fibonacci(n):
    #print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@cache
def test2(n):
    return n*2

#print([fibonacci(n) for n in range(1, 9)])
[fibonacci(n) for n in range(1, 9)]

print ([test2(n) for n in range(1, 9)])


