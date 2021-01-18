import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
	client.subscribe("gpio/#")

def on_message(client, userdata, msg):
	print("Ok " + str(msg.payload))
	if str(msg.payload) == "b'1'":
		client.publish("led/504", "1")
		time.sleep(0.5)
	else:
		client.publish("led/504", "0")
		time.sleep(0.5)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
