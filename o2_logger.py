#!/usr/bin/python

import time, os



def logMessage(status):
                
  print( "::::" )
  print (":::: ",status['dateTime']," :::: ",status['message']," ::::")
  for x in status:
	print(x, status[x])
	
  


