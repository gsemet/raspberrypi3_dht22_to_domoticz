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
