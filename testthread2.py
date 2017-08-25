

import threading
import time


txt = ''

def input_reader(backend, a):
    print "starting ", backend, a
    global txt
    while 1:
        txt = raw_input()
        if txt == 'q':
            break

def input_writter():
    lasttxt = '.'
    while 1:
        time.sleep(2)
        #if lasttxt == txt: continue
        lasttxt = txt
        print "input_writter", txt
        if txt == 'q':
            break

help(threading)
test = 'BACKEN'
test2 = 'azd'
t1 = threading.Thread(target=input_reader, args=(test, test2))
t1.start()

t2 = threading.Thread(target=input_writter)
t2.start()








