## INSTALATION

#1 - Copy this script file to "/storage/UserScripts/shutdown.py"
#2 - Execute "nano /storage/.config/autostart.sh"
#3 - Write in "python /storage/UserScripts/shutdown.py &"
#4 - Copy de RPi folder to "/storage/lib/"
#5 - Restart the Kodi

#The next two lines are required for the OpenElec - Kodi
import sys
sys.path.append('/storage/lib')

import RPi.GPIO as GPIO  
import time  
import os  

#Setup for I/O from GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,GPIO.HIGH) #Led
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.LOW) #Cooler
wLed = True

##Main function - Shutdown  

# Press the button: wLed On/Off;
# Hold the button less than 6s: Reboot;
# Hold the button more than 1.5s and less than 6s: Turn off

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
		os.system("sudo shutdown -h now")
	elif tCounter > 15:
		print("Reiniciar!")
		os.system("sudo reboot")
	else:
		global wLed
		if wLed:
			wLed = False
			GPIO.output(13,GPIO.LOW)
		else:
			wLed = True
			GPIO.output(13,GPIO.HIGH)
# Watch for the button event
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  


while 1:  
	time.sleep(1)