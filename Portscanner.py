#!/bin/python

import sys
import socket

from datetime import datetime

#Define out Target
#Basic Port Scanner

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
	print(target)
else:
	print('Invalid amount of arguments\n')
	print('Usage: python3 Portscanner.py <Hostname>')

print("-"*50)
print("Scanning the Target: {}".format(target))
print("Time Started: {}".format(datetime.now()))
print("-"*50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {} is Open".format(port))
		s.close()
#python3 scanner.py <ip>
except KeyboardInterrupt:
	print("User Interupted the Process\n")
	sys.exit()
except socket.gaierror:
	print("Hostname Could not be Resolved\n")
	sys.exit()
except socket.error:
	print("Couldnt Connect to the server\n")
	sys.exit()