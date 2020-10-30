# hardware_

This is the hardware repo for the [My Solar Garden App](insert link here). The My Solar Garden app allows users to track the health of their gardens through light, temperature, and humidity sensors connected to RaspberryPis. In this repo you will find all the necesary hardware and scripts to connect your own sensors to the My Solar Garden App.

## Table of Contents
1. Compatible Hardware
2. Setup
3. Versions
4. Contributors


## Compatible Hardware

- RaspberryPi Model 3 or Higher (insert link)
- GrovePi Sensors
    - Temperature & Humidity Sensor v1.2 (insert link)
    - Light Sensor v1.2 (insert link)
- GrovePi Accessories
    - LED Bar v2.0 (insert link)
    
## Setup

Tech Setup
- clone this repo to your RaspberryPi
- Run the following on your initial set up to configure the program with the sensor ids registered on the My Solar App (link to sensor id page?)
    - `python insert_sensor_ids.py` insert your ids on the command line
- `python start_sensors.py`

Physical Setup
- Plug in the RaspberryPi to a power source
- Plug the following components to the specified ports on the RaspberryPi:
    - Port D2: Temperature and Humitidy Sensor
    - Port A0: Light Sensor
    - Port D4: LED bar
- Place the sensors near your garden (insert pictures)
