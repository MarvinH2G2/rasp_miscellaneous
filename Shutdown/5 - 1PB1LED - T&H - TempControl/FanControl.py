# Raspberry Fan Control

import os 
import time 
import sys
import RPi.GPIO as GPIO 

sys.path.append('/storage/lib')

#Setup for I/O from GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.LOW) #Cooler
fan = False

# Return CPU temperature as a character string                                      
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	res = res.replace("temp=","").replace("'C\n","")
	return(int(float(res)))

# Do a loop to wait for the button press or temperature changes
while 1:  
	cputemp = getCPUtemperature()
	print (cputemp)
	global fan
	if cputemp > 10:
		print("Turn fan on") 
		fan = True
		GPIO.output(27,GPIO.HIGH)
	elif cputemp < 5:
		print("Turn fan off")
		fan = False
		GPIO.output(27,GPIO.LOW)
	time.sleep(1)