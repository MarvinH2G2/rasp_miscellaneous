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
fan = False

##Main function - Shutdown  

# Press the button: Fan On/Off;
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
# Watch for the button event
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  

# Secundary function - Temp control
# Return CPU temperature as a character string                                      
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	res = res.replace("temp=","").replace("'C\n","")
	return(int(float(res)))

# Do a loop to wait for the button press or temperature changes
while 1:  
	cputemp = getCPUtemperature()
	print cputemp
	global fan
	if cputemp > 60:
		fan = True
		GPIO.output(27,GPIO.HIGH)
	elif cputemp < 40:
		fan = False
		GPIO.output(27,GPIO.LOW)
	time.sleep(1)