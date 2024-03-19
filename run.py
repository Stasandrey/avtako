#! /usr/bin/python3
import paho.mqtt.client as paho
import random

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client_id = f'python-mqtt-{ random.randint(0, 1000)}'

client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.username_pw_set("homeassistant", "baziliy")
client.on_connect = on_connect
print(client.connect("192.168.100.77", 1883))

client.publish("test", "10", qos=2)
print("111")