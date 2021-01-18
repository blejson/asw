#!/usr/bin/env python3.6
import time
import gpio
print("Test LED@PWM0\n")
gpio.setup(504, gpio.OUT)
gpio.setup(488, gpio.IN)
dioda_stan = 1
while(True):
	if gpio.read(488) == 1:
		gpio.set(504, dioda_stan)
		if dioda_stan == 1:
			dioda_stan = 0
		else:
			dioda_stan = 1
		time.sleep(2)

