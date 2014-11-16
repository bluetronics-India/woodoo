import RPi.GPIO as GPIO
import re
import os

WORDS = ["Wireless","Test"]

def handle(text, mic, profile):

	os.call('screen /dev/ttyS0 19200,cs8')

def isValid(text):
    return bool(re.search(r'\bwireless\b', text, re.IGNORECASE)) or bool(re.search(r'\bTest\b', text, re.IGNORECASE))
