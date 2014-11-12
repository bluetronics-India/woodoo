import RPi.GPIO as GPIO
import re

from wordConverter import WordConverter

WORDS = ["TURN", "PIN","ON"]

def handle(text, mic, profile):

    WC = WordConverter()

    split = text.split(" ")

    pin = WC.convertToInteger(pin)
    mic.say("Which Pin?")

    result = mic.activeListen()
    pin = WC.convertToInteger(result)



    GPIO.setmode(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)

def isValid(text):
    return bool(re.search(r'\bturn pin on\b', text, re.IGNORECASE))
