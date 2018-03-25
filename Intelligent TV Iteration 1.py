#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

TRIG = 11
ECHO = 12
BUZZ = 13

def setup(pin):
        global BuzzerPin
        BuzzerPin = pin
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.setup(BuzzerPin, GPIO.OUT)
	GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
        GPIO.output(BuzzerPin, GPIO.LOW)

def off():
        GPIO.output(BuzzerPin, GPIO.HIGH)

def beep(x):
        on()
        time.sleep(x)
        off()
        time.sleep(x)
        
def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	while True:
		dis = distance()
		if dis < 100:
                        beep(1)
		print dis, 'cm'
		print ''
		time.sleep(0.3)

def destroy():
        GPIO.output(BuzzerPin, GPIO.HIGH)
	GPIO.cleanup()

if __name__ == "__main__":
	setup(BUZZ)
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
