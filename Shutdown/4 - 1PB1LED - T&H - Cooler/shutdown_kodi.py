#The next two lines are required for the OpenElec - Kodi
import sys
sys.path.append('/storage/lib')

import RPi.GPIO as GPIO  
import time  
import os  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,GPIO.HIGH)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.HIGH)
fan = True

# Our function on what to do when the button is pressed  
def Shutdown(channel):
	bTest = True
	tCounter = 0
	while bTest:
		tCounter = 1 + tCounter
		time.sleep(0.1)
		if bool(tCounter & 1):
			GPIO.output(13,GPIO.HIGH)
		elif tCounter > 60:
			GPIO.output(13,GPIO.HIGH)
		else:
			GPIO.output(13,GPIO.LOW)
		print(tCounter)
		if (GPIO.input(18)):
			bTest = False
		else:
			bTest = True
	if tCounter > 60:
		print("Desligar!")
		os.system("shutdown -h now")
	elif tCounter > 15:
		print("Reiniciar!")
		os.system("reboot")
	else:
		global fan
		if fan:
			GPIO.output(27,GPIO.LOW)
			fan = False
			GPIO.output(13,GPIO.HIGH)
		else:
			GPIO.output(27,GPIO.HIGH)
			fan = True
			GPIO.output(13,GPIO.HIGH)
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
 
# Now wait!  
while 1:  
    time.sleep(1)