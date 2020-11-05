# [My Solar Garden](https://solar-garden-fe.herokuapp.com/) - Hardware

This is the hardware repo for the [My Solar Garden App](https://solar-garden-fe.herokuapp.com/). The My Solar Garden app allows users to track the health of their gardens through light, temperature, and moisture sensors connected to RaspberryPis. In this repo you will find all the necesary hardware and scripts to connect your own sensors to the My Solar Garden App.

## Table of Contents
1. [Compatible Hardware](#hardware)
2. [Setup](#setup)
3. [Undestanding Sensor Readings](#readings)
4. [Contributors](#contributors)


## Compatible Hardware <a name="hardware"></a>

- [RaspberryPi Model 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/?resellerType=home) or Higher 
- GrovePi Sensors:
    - [Temperature & Humidity Sensor v1.2](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/#features)
    - [Light Sensor v1.2](https://wiki.seeedstudio.com/Grove-Light_Sensor/)
    - [Soil Moisture Sensor](https://www.seeedstudio.com/Grove-Moisture-Sensor.html)
- GrovePi Accessories
    - [LED Bar v2.0](https://wiki.seeedstudio.com/Grove-LED_Bar/)
    
## Setup <a name="setup"></a>

#### RaspberryPi Setup
- `git clone git@github.com:My-Solar-Garden/hardware_.git`
- Run the following on your initial set up to configure the program with the sensor IDs registered on the My Solar App
    - `curl -kL dexterindustries.com/update_grovepi | bash`
    - `cd /home/pi/Dexter/GrovePi/Firmware`                 
    - `bash firmware_update.sh`                             
    - `sudo gem install i2c i2c-devices`                    
    - `pip install requests`
    - `python sensors.py`: insert your sensor IDs on the command line and watch the sensors output data to the production database!
    - Sensor IDs can be found on your garden page in the My Solar Garden App

#### Physical Setup
- Plug the following components to the specified ports on the RaspberryPi:
    - Port D2: Temperature and Humitidy Sensor
    - Port A0: Light Sensor
    - Port D4: LED bar
- Plug in the RaspberryPi to a power source
- Place the sensors near your garden

#### RaspberryPi Tips
- Connect your Raspberry Pi to a monitor through an HDMI cable, a usb keyboard and connect any sensors you would like to use
- Connect to power last, as sensors can be damaged if plugged in after the power is on.
- Connect to your Wifi by running `raspi -config` and entering your Wifi's name and password. 
- Connect to your Raspberry Pi on your mac's terminal by running `ssh pi@<your ip>` and cd into the repo 

## Understanding Sensor Readings <a name="hardware"></a>
    - Sensor readings are being posted to the production database, so any sensor readings in test/development will have to be mocked
#### Light Sensor:
    - no/very little light: 0
    - dim: 30-100
    - mid-level: 200-500
    - bright: 500-740
    - very bright: 740-770 (This is basically any direct sunlight on the sensor)
    
#### Temperature Sensor:
    - Returns degrees in celcius
    
#### Moisture Sensor

## Contributors
In no particular order:

