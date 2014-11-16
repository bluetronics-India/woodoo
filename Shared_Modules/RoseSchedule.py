# -*- coding: utf-8-*-
import random
import re

WORDS = ["ROSE", "SCHEDULE"]

PRIORITY = 5

blockTimes = []
earlyResponse = "Classes haven't started yet today"
lateResponse = "Classes are over for the day"
pTime = "It is Passing Time"
blocks = ["First","Second","Third","fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth"]

responses = []
for a in blockes:
    responses.add("It is {0} period".format(a))

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    b = datetime.datetime.now()

    a = datetime.datetime(b.year,b.month,b.day,8,5)

    if(b<a):
        mic.say(earlyResponse)
        return

    for i in range(10):
        a = a + datetime.timedelta(0,3000)
        if(b<a):
            mic.say(responses[i])
            return
        a = a + datetime.timedelta(0,300)
        if(b<a):
            mic.say(pTime)
            return

    if(b<a):
        mic.say(lateResponse)
        return


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\brose\b', text, re.IGNORECASE)) and bool(re.search(r'\brose\b', text, re.IGNORECASE))
