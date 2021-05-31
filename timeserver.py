'''time server'''

'''all three done in the same directory'''

nano timeserver.py

#!user/bin/env python3


''' Server for day and time using our client handler'''

from socket import *
from timeclienthandler import timeclienthandler


HOST = "localhost"
PORT = 2500
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(7)

#Server wating for connections

while True:
	print("waiting for a connection...")
	client, address = server.accept()
	print("connected from: ", address)
	handler = TimeClientHandler(client)
	handler.start()

