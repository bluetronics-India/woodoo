import RPi.GPIO as GPIO
import re
import os

WORDS = []
priority = 50
location = "/home/pi/NodeRedSave"

def handle(text, mic, profile):
'''
Always runs and always writes file to disk
'''

	value = 0
	fName = location+"/tempFile"+str(value)
	while(not os.path.isfile(fName)):
		value+=1
		fName = location+"/tempFile"+str(value)

	f = open(fName)
	f.write(text)
	f.close()

def isValid(text):
	return True
