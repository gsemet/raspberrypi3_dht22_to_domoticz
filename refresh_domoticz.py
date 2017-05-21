#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import yaml

from dhtxx import DHT22
from time import sleep


def read_dht22(pin):
    # Adjust pin (BCM) for your needs !
    dht22 = DHT22(pin)
    return dht22.get_result_once()

if __name__ == '__main__':
    with open("config.yaml") as f:
        config = yaml.load(f)
    temp, humi = read_dht22(config.pin)
    print(temp)
    print(humi)
