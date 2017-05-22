#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os

import Adafruit_DHT
import requests


DOMOTICZ_IP = '192.168.0.37'
DOMOTICZ_PORT = '80'
DOMOTICZ_ROOT = '/domoticz'
DOMOTICZ_USER = ''
USE_DOT_DOMOTPWD = True
DOMOTICZ_PASSWORD = ''
DOMOTICZ_VIRTUAL_IDX = 221

SENSOR = Adafruit_DHT.DHT22
PIN = 13

def read_dht22(pin):
    # Adjust pin (BCM) for your needs !
    try:
        logging.debug("Reading DHT%d on pin %d", SENSOR, pin)
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, pin)
        logging.debug("Temperature: %s, humidity: %s", temperature, humidity)
        return humidity, temperature
    except RuntimeError:
        logging.exception("Have you enabled 'device-tree' mode in `raspi-config` ?")
        raise



def update_domoticz(temperature, humidity):
    requete = ('http://{ip}:{port}{root}/json.htm?type=command&param=udevice&idx={idx}'
               '&nvalue=0&svalue={temp:.2f};{humi:.2f};2'
               .format(ip=DOMOTICZ_IP,
                       port=DOMOTICZ_PORT,
                       root=DOMOTICZ_ROOT,
                       idx=DOMOTICZ_VIRTUAL_IDX,
                       temp=temperature,
                       humi=humidity))
    logging.debug("Request: %r", requete)
    user = DOMOTICZ_USER
    password = DOMOTICZ_PASSWORD
    if USE_DOT_DOMOTPWD:
        with open(os.path.expanduser("~/.domotpwd")) as f:
            user = f.readline().strip()
            password = f.readline().strip()
    res = requests.get(requete, auth=requests.auth.HTTPBasicAuth(user, password))
    if res.status_code != 200:
        logging.error("Erreur API Domoticz: %s", res.status_code)
    else:
        logging.debug("Success")


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(levelname)-7s - %(message)s',)
    humi, temp = read_dht22(PIN)
    update_domoticz(temp, humi)


if __name__ == '__main__':
    main()
