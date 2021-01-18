import paho.mqtt.client as mqtt
import gpio

gpio.setup(504, gpio.OUT)

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("led/#")

def on_message(client, userdata, msg):
	print(str(msg.payload) + "XDDDDD")
	if str(msg.payload) == "b'1'":
		print("ON")
		gpio.set(504, 1)
	else:
		print("OFF")
		gpio.set(504, 0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()
