#!/usr/bin/python3
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall

def get_data():
    data = check_output(["sudo","bash","/home/andrey/avtako/hdd.sh"]).decode("UTF-8")
    return(findall("\d+",data)[0])

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname="192.168.100.83")

data = get_data()
publish_message("/orange/hdd", data)