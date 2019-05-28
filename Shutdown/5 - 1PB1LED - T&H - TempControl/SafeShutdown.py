import RPi.GPIO as GPIO  
import time  
import os  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("----------------------------")
print("Rodando SafeShutDown...")
print("----------------------------")

# Our function on what to do when the button is pressed  
def Shutdown(channel):
    print("Sistema vai desligar em 3 segundos...")
    time.sleep(3)
    os.system('cls' if os.name=='nt' else 'clear')
    print("Desligando...")
    os.system("shutdown -h now")

# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  

# Now wait! 
i = 1
while 1:
    # print(i, end='\r')
    # i = i + 1
    time.sleep(1)