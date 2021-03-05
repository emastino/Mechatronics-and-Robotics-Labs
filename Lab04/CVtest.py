import RPi.GPIO as GPIO
import cv2 as cv
import numpy as np
import time as sleep

Rasp1 = 2

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(Rasp1,GPIO.OUT)
GPIO.output(Rasp1,0)

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_green = np.array([60,150,100])
    upper_green = np.array([65,200,255])
    mask = cv.inRange(hsv,lower_green,upper_green)
    res = cv.bitwise_and(frame,frame,mask = mask)
    imgHeight, imgWidth,_ = hsv.shape
    IsGreen = np.sum(mask)
#     GPIO.output(3,0)
    GPIO.output(Rasp1,0)

    if IsGreen > 5000:
        GPIO.output(Rasp1,1)
        print(IsGreen)
#         sleep.sleep(0.1)
 
#     cv.imshow('Test',frame)
#     cv.imshow('mask',mask)
    cv.imshow('res',res)
    if cv.waitKey(5) and 0xFF ==ord('x'):
        break

cv.destroyAllWindows()
GPIO.cleanup()