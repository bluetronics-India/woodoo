import RPi.GPIO as GPIO
import re
import os

WORDS = ["TOGGLE","LIGHT","ON","OFF"]

def handle(text, mic, profile):

	if(bool(re.search(r'\bON\b', text, re.IGNORECASE))):
		os.call('screen /dev/AMA0 9600,cs8\nr1 r1r1r1')
	else:
		os.call('screen /dev/AMA0 9600,cs8\n r0 r0r0r0')

def isValid(text):
    return bool(re.search(r'\bTOGGLE LIGHT\b', text, re.IGNORECASE)) or bool(re.search(r'\bTest\b', text, re.IGNORECASE))
