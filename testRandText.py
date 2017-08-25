from __future__ import print_function

import random
import time


def main():
    my_base_text = 'More than cleverness we need kindness and gentleness.'
    my_rand_text = ''


    while my_rand_text != my_base_text:
        my_rand_text = iterate(my_base_text, my_rand_text)
        print (my_rand_text)
        time.sleep(0.005)



def random_letter():
    return chr(random.randint(32,127))

rand_text = ''



# recursion would be a solution but due to python bad TRE, recursion must better be avoided
def iterate(base_text, rand_text):
    new_text = ''
    for idx, x in enumerate(base_text):
        if len(rand_text) != len(base_text) or x != rand_text[idx]:
            new_text = new_text + random_letter()
        else:
            new_text = new_text + rand_text[idx]

    return new_text

if __name__ == '__main__':
    main()


