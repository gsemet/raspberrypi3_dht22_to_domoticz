#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import Adafruit_DHT
import requests


DOMOTICZ_IP = '192.168.0.37'
DOMOTICZ_PORT = '8080'
DOMOTICZ_ROOT = '/domoticz'
USER = ''
PASSWORD = ''
DOMOTICZ_IDX = 221

SENSOR = 22
PIN = 18

def read_dht22(pin):
    # Adjust pin (BCM) for your needs !
    try:
        logging.debug("Reading DHT%d on pin %d", SENSOR, pin)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return humidity, temperature
    except RuntimeError:
        logging.exception("Have you enabled 'device-tree' mode in `raspi-config` ?")
        raise



def update_domoticz(temperature, humidity):
    requete = ('http://{ip}:{port}{root}/json.htm?type=command&param=udevice&idx={idx}'
               '&nvalue=0&svalue={temp}:{humi};2'
               .format(ip=DOMOTICZ_IP,
                       port=DOMOTICZ_PORT,
                       idx=DOMOTICZ_IDX,
                       temp=temperature,
                       humi=humidity))
    logging.debug("Request: %r", requete)
    res = requests.get(requete, auth=requests.auth.HTTPBasicAuth(USER, PASSWORD))
    if res.status_code != 200:
        logging.error("Erreur API Domoticz: %s", res.status_code)


def main():
    humi, temp = read_dht22(14)
    update_domoticz(temp, humi)


if __name__ == '__main__':
    main()
