import RPi.GPIO as GPIO
import re
import os

WORDS = ["TOGGLE","LIGHT","ON","OFF"]

def handle(text, mic, profile):

	if(bool(re.search(r'\bON\b', text, re.IGNORECASE))):
		os.call('screen /dev/AMA0 1200,cs8\n111111111111111111111')
	else:
		os.call('screen /dev/AMA0 1200,cs8\n000000000000000000000')

def isValid(text):
    return bool(re.search(r'\bTOGGLE LIGHT\b', text, re.IGNORECASE)) or bool(re.search(r'\bTest\b', text, re.IGNORECASE))
