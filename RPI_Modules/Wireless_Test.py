import re
import serial
//Some comments
WORDS = ["RED","GREEN","BLUE","ONE","ZERO"]

def handle(text, mic, profile):

	if( bool(re.search(r'\bRED\b', text, re.IGNORECASE))):
		txt = "r"
	elif(bool(re.search(r'\bBLUE\b', text, re.IGNORECASE)) ):
		txt="b"
	elif(bool(re.search(r'\bGREEN\b', text, re.IGNORECASE)) ):
		txt="g"
	else:
		break

	if( bool(re.search(r'\bONE\b', text, re.IGNORECASE))):
		e="1"
	elif(bool(re.search(r'\bZERO\b', text, re.IGNORECASE)) ):
		e="0"
	else:
		break

	ser = serial.Serial('/dev/ttyAMA0',9600)
	ser.write(txt)
	time.sleep(0.050)
	ser.write(e)

def isValid(text):
    return bool(re.search(r'\bRED\b', text, re.IGNORECASE)) or bool(re.search(r'\bBLUE\b', text, re.IGNORECASE)) or bool(re.search(r'\bGREEN\b', text, re.IGNORECASE))
