#! /usr/bin/python3

import datetime
import psutil

HOST = "192.168.100.77"
USER = "homeassistant"
PASSWORD = "baziliy"

# Список всех публикуемых параметров группы SERVER
server = {"boot_time": "",
          "memory_usage": "",
          "disk_usage": "",
          "cpu_temp": "",
          "cpu_usage": ""
          }


# Публикует сообщение
def mqtt_pub(topic, message):
    import os
    cmd_line = "mosquitto_pub -h %s -t %s -m %s -u %s -P %s" % (HOST, topic, message,
                                                                USER, PASSWORD)
    os.system(cmd_line)


def run():
    mqtt_pub("test", "hello")


if __name__ == "__main__":
    # run()
    server["boot_time"] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
                                                                    "%Y-%m-%d %H:%M:%S")
    server["memory_usage"] = psutil.virtual_memory().percent
    server["disk_usage"] = psutil.disk_usage('/').percent
    server["cpu_temp"] = psutil.sensors_temperatures()["coretemp"][0].current
    server["cpu_usage"] = psutil.cpu_percent(interval=0.1, percpu=False)

    print(server)

else:
    print("This program must be run as __main__.")
