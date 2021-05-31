
nano Timehandler.py 

#!/usr/bin/env python 3
''''
This will provide day and time 

'''

from time import ctime
from threading import Thread
from codecs import decode 

'''Creating the time handler class'''
class TimeClientHandler(Thread):
	'''Handles the request from the client'''
	def __init__(self, client):
	   Thread.__init__(self)
	   self.client = client

	def run(self):
		self.client.send(bytes(ctime() + '\nHave a great day, Bailey!', "ascii"))

		self.client.close()