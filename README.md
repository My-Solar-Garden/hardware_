# hardware_

This is the hardware repo for the [My Solar Garden App](insert link here). The My Solar Garden app allows users to track the health of their gardens through light, temperature, and humidity sensors connected to RaspberryPis. In this repo you will find all the necesary hardware and scripts to connect your own sensors to the My Solar Garden App.

## Table of Contents
1. Compatible Hardware
2. Setup
3. Sensor Readings Context
4. Contributors


## Compatible Hardware

- [RaspberryPi Model 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/?resellerType=home) or Higher 
- GrovePi Sensors
    - [Temperature & Humidity Sensor v1.2](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/#features)
    - [Light Sensor v1.2](https://wiki.seeedstudio.com/Grove-Light_Sensor/)
- GrovePi Accessories
    - [LED Bar v2.0](https://wiki.seeedstudio.com/Grove-LED_Bar/)
    
## Setup

Tech Setup
- clone this repo to your RaspberryPi
- Run the following on your initial set up to configure the program with the sensor ids registered on the My Solar App (link to sensor id page?)
    - Connect your Raspberry Pi to a monitor through an HDMI cable, a usb keyboard and connect any sensors you would like to use. Make sure to attach the power last, as sensors can be damaged if plugged in after the power is on.
    - Connect to your Wifi by running `raspi -config` and entering your Wifi's name and password. 
    - Connect to your Raspberry Pi on your mac's terminal by running `ssh pi@<your ip>` and cd into the repo 
    - `curl -kL dexterindustries.com/update_grovepi | bash` Do we need to run these commands on initial setup?
    - `cd /home/pi/Dexter/GrovePi/Firmware`                 ?
    - `bash firmware_update.sh`                             ?
    - `sudo gem install i2c i2c-devices`                    or will these updates be installed on the repo?
    - `pip install requests`
    - `python sensors.py` and insert your sensor ids on the command line and watch the sensors output data to the production database!

Physical Setup
- Plug the following components to the specified ports on the RaspberryPi:
    - Port D2: Temperature and Humitidy Sensor
    - Port A0: Light Sensor
    - Port D4: LED bar
- Plug in the RaspberryPi to a power source
- Place the sensors near your garden (insert pictures)

## Sensor Readings Context
    - Sensor readings are being posted to the production database, so any sensor readings in test/development will have to be mocked
### Light Sensor:
    - no/very little light: 0
    - dim: 30-100
    - mid-level: 200-500
    - bright: 500-740
    - very bright: 740-770 (This is basically any direct sunlight on the sensor)
    
### Temperature Sensor:
    - Returns degrees in celcius
