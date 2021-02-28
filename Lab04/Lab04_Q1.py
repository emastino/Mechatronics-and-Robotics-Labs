import RPi.GPIO as GPIO # import the GPIO library
import time # import time library
import cv2 # import open cv for testing purpases

# function for LED light ups when a leve is won
def passLevel(leds, times):
    for i in range(times):
        for i in leds:
            GPIO.output(i, True)
                #print(i)
        time.sleep(0.1)
        for i in leds:
            GPIO.output(i, False)
                #print(i)
        time.sleep(0.1)
        
# button
rightButton = 23

#LED counter
counter = -1;

# level counter
levelCounter =0;

## Pin set up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # use BCMf numbering for the pins on the Pi
                        # because BMC is universal
LEDs = [24,25,8,7,12,16,20]
# Pin Setup
GPIO.setup(rightButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # internal resistor as
                                                            # pull down resistor
for i in LEDs:
    GPIO.setup(i, GPIO.OUT)
#    print(i)

loopControl = True

while loopControl:
    counter = (counter+1)%7 
    print(GPIO.input(rightButton))
    GPIO.output(LEDs[counter],True)
    time.sleep(0.3 -levelCounter/15)
    

    if(GPIO.input(rightButton)==1): # high when pressed
        # pressed when gree
        if counter == 3:
            
            counter = -1
            passLevel(LEDs, 3)
            if levelCounter == 3:
                loopControl = False
                print(" YOU WIN ")
                break
            levelCounter = levelCounter+1
#         print(counter)
        else:
            counter = -1 # reset counter 
        time.sleep(0.3)
    for i in LEDs:
        GPIO.output(i, False)        
    
    
GPIO.cleanup()
