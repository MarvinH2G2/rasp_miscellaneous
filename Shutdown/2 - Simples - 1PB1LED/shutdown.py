import RPi.GPIO as GPIO  
import time  
import os  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  
GPIO.setup(13,GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.output(13,GPIO.HIGH)

# Our function on what to do when the button is pressed  
def Shutdown(channel):
    os.system("sudo shutdown -h now")
 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
 
# Now wait!  
while 1:  
    time.sleep(1)
