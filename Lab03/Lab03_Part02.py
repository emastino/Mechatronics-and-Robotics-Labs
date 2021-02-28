import RPi.GPIO as GPIO # import the GPIO library
import time
import cv2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # use BCMf numbering for the pins on the Pi
                        # because BMC is universal
rightButton = 23
counter = 0;

LEDs = [24,25,8]
# Pin Setup
GPIO.setup(rightButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # internal resistor as
                                                            # pull down resistor
for i in LEDs:
    GPIO.setup(i, GPIO.OUT)
#    print(i)

loopControl = True

while loopControl:
    if counter == 0:
        for i in LEDs:
            GPIO.output(i, False)
            #print(i)
    if(GPIO.input(rightButton)==1): # high when pressed
        counter = (counter +1)%4
        print(counter)
        time.sleep(0.3)
        
    for i in range (counter):
        GPIO.output(LEDs[i],True)
    
GPIO.cleanup()

