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

	fName = location+"/logFile.txt"
	f = open(fName,"w")
	f.write(text)
	f.close()

def isValid(text):
	return True
