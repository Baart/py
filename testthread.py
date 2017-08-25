#
import threading 
import Queue
import time

q = Queue.Queue()
tab = []

def display(nb, q, nom=""):
	for i in range(nb):
		q.put(nom)


for i in range(97, 123, 1):
	t = threading.Thread(None, display, None, (100,q,chr(i)))
	tab.append(t)

for t in tab:
	t.start()

for t in tab:
	t.join()

result = ""
while(not q.empty()):
	result += q.get()

print result
print "end of all threads"
