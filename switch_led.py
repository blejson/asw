import paho.mqtt.client as mqtt
import time
import gpio
gpio.setup(488, gpio.IN)
client = mqtt.Client()
client.connect("localhost", 1883, 60)
while(True):
	if gpio.read(488) == 1:
		client.publish("led/504", "1")
		time.sleep(0.5)
	else:
		client.publish("led/504", "0")
		time.sleep(0.5)
