#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pathlib import Path
from time import sleep

from dhtxx import DHT22


def read_dht22(pin):
    # Adjust pin (BCM) for your needs !
    dht22 = DHT22(pin)
    return dht22.back()

if __name__ == '__main__':
    temp, humi = read_dht22(14)
    print(temp)
    print(humi)
