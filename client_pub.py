import paho.mqtt.client as mqtt
import time

# This is the Publisher
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))


client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect

client.publish("topic/test", "Hello world!")
time.sleep(2)
client.disconnect()

def print:
	print("Sanjay from sample 1")