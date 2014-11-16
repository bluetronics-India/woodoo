import RPi.GPIO as GPIO
import re

WORDS = ["TURN", "PIN","ON","OFF"]
values = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
WORDS.extend(values)

def handle(text, mic, profile):

    if(bool(re.search(r'\bon\b', text, re.IGNORECASE))):
        result = "ON"
    else:
        result = "OFF"

    WC = WordConverter()

    split = text.split(" ")

    pin = WC.convertToInteger(pin)
    mic.say("Which Pin?")

    result = mic.activeListen()

    result = values.index(result)

    GPIO.setmode(pin,GPIO.OUT)

    if(result=="ON"):
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin,GPIO.LOW)

def isValid(text):
    result = bool(re.search(r'\bturn pin\b', text, re.IGNORECASE))
    if(result == False):
        return False
    return bool(re.search(r'\bon\b', text, re.IGNORECASE)) or bool(re.search(r'\boff\b', text, re.IGNORECASE))
