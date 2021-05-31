'''time server'''

nano timeclient.py

#!/usr/bin/env python3


from socket import *
from codecs import decode

HOST = "localhost"
PORT = 2500
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

try	server = socket(AF_INET, SOCK_STREAM)
 	server.connect(ADDRESS)
 	TimeAndDay = decode(server.recv(BUFSIZE), "ascii")
 	print(TimeAndDay)
 	server.close()
except ConnectionRefusedError:
	print("There seems to be an error connecting to the server.")

