'''
simple socket test example
'''


import socket
import sys

import time
from threading import Thread



def check_server(address, port):
	# Create a TCP socket
	s = socket.socket()
	#print "Attempting to connect to %s on port %s" % (address, port)
	try:
		s.connect((address, port))
		#print "Connected to %s on port %s" % (address, port)
		return True
	except socket.error, e:
		#print "Connection to %s on port %s failed: %s" % (address, port, e)
		return False

from socket import *

def checkPort(address, port):
	# create a raw socket and bind it to the public interface
	s = socket(AF_INET, SOCK_RAW, IPPROTO_IP)
	s.bind((address, 0))

	# Include IP headers
	s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

	# receive all packages
	s.ioctl(SIO_RCVALL, RCVALL_ON)

	# receive a package
	try:
		print s.recvfrom(21)
	except:
		pass
	# disabled promiscuous mode
	s.ioctl(SIO_RCVALL, RCVALL_OFF)


	if 0:
	    s = socket(AF_INET, SOCK_STREAM)
	    s.settimeout(5)
	    result = s.connect_ex((address, i))
	    if(result == 0):
			print 'Port %d: OPEN' % (i,)
			print "send result", s.send("test")
			return True
	    s.close()
	    return False
	return False


for i in range(1,65536):
	#pass
	#t = Thread(target=checkPort, args=(gethostbyname("khadockserv.no-ip.biz"),i))
	t = Thread(target=checkPort, args=(gethostbyname("127.0.0.1"),i))
	t.start()

