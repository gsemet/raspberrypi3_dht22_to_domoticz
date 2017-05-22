=========================
DHT22 refresh to domoticz
=========================

A little script that read a DHT22 temperature and humidity sensor connected to a GPIO
of a Raspberry Pi 3 and send the value to a virual sensor in Domoticz (local or remote).

Note: This will set up a virtualenv for Python script to be isolated from the rest of
your system. This is a good habit to get, avoid setting up libraries all over the place, let
`pip install` mess the system's Python install. 

Wiring
======

Use schema in Adafruit: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/wiring

Tested with a DHT22 and a Raspberry Pi 3

Installation:
=============

Reference: https://easydomoticz.com/dht-11-22-raspberry-ca-marche-enfin/

- clone this project to your Raspberry Pi
- execute `./install.sh`
- edit the python script according to your configuration
- add this line to your crontab (use `sudo crontab -e`):

    */5 * * * * /path/to/raspberrypi3_dht22_to_domoticz/run.sh

Note: HTTP password can be put in ~/.domotpwd file instead of hardcoded in the script, with
the following format:

    username
    password
