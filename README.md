# [My Solar Garden](https://solar-garden-fe.herokuapp.com/) - Hardware

This is the hardware repo for the [My Solar Garden App](https://solar-garden-fe.herokuapp.com/). The My Solar Garden app allows users to track the health of their gardens through light, temperature, and humidity sensors connected to RaspberryPis. In this repo you will find all the necessary hardware and scripts to connect your own sensors to the My Solar Garden App.

## Table of Contents
1. [Compatible Hardware](#hardware)
2. [Setup](#setup)
3. [Undestanding Sensor Readings](#readings)
4. [Contributors](#contributors)


## Compatible Hardware <a name="hardware"></a>

- [RaspberryPi Model 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/?resellerType=home) or Higher
- [GrovePi+ Board](https://www.seeedstudio.com/GrovePi.html)
- GrovePi Sensors:
    - [Temperature & Humidity Sensor v1.2](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/#features)
    - [Light Sensor v1.2](https://wiki.seeedstudio.com/Grove-Light_Sensor/)
<img src="https://user-images.githubusercontent.com/56651612/98299629-42f63b00-1f75-11eb-8d4d-0ac871ef4e7c.jpeg" height="600">   

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
<img src="https://user-images.githubusercontent.com/56651612/98299664-4c7fa300-1f75-11eb-9d0d-257454e643c2.jpeg" height="600">   
- Plug the following components to the specified ports on the RaspberryPi:
    - Port D2: Temperature and Humitidy Sensor
    - Port A0: Light Sensor
- Plug in the RaspberryPi to a power source
- Place the sensors near your garden

#### RaspberryPi Tips
- Connect your Raspberry Pi to a monitor through an HDMI cable, a usb keyboard and connect any sensors you would like to use
- Connect to power last, as sensors can be damaged if plugged in after the power is on.
- Connect to your Wifi by running `raspi -config` and entering your Wifi's name and password.
- Connect to your Raspberry Pi to your mac's terminal by running `ssh pi@<your ip>` from the command line and cd into the repo

## Understanding Sensor Readings <a name="readings"></a>
   - Sensor readings are being posted to the production database, so any sensor readings in test/development will have to be mocked
#### Light Sensor:
   - no/very little light: 0
   - dim light: 30-100
   - mid-level light: 200-500
   - bright light: 500-740
   - very bright light: 740-770 (This is basically any direct sunlight on the sensor)

#### Temperature Sensor:
   - Returns degrees in celcius

## Contributors
  * Alex Desjardins
    * [GitHub](https://github.com/moosehandlr)
    * [LinkedIn](https://www.linkedin.com/in/alex-desjardins-59297b8b/)
  * Angela Guardia
    * [GitHub](https://github.com/AngelaGuardia)
    * [LinkedIn](https://www.linkedin.com/in/angela-guardia/)
  * Danielle Coleman
    * [GitHub](https://github.com/dcoleman21)
    * [LinkedIn](https://www.linkedin.com/in/danielle-coleman-86ab3b13/)
  * Daniel Lessenden
    * [GitHub](https://github.com/D-Lessenden)
    * [LinkedIn](https://www.linkedin.com/in/lessenden/)
  * Drew Williams
    * [GitHub](https://github.com/drewwilliams5280)
    * [LinkedIn](https://www.linkedin.com/in/drewwilliams5280/)
  * Eric Hale
    * [GitHub](https://github.com/EHale64)
    * [LinkedIn](https://www.linkedin.com/in/eric-hale-656843155/)
  * Hashim Gari
    * [GitHub](https://github.com/hashmaster3k)
    * [LinkedIn](https://www.linkedin.com/in/hashim-gari/)
  * Leah Riffell
    * [GitHub](https://github.com/leahriffell)
    * [LinkedIn](https://www.linkedin.com/in/leah-riffell/)
  * Logan Riffell
    * [GitHub](https://github.com/lkriffell)
    * [LinkedIn](https://www.linkedin.com/in/logan-riffell/)
  * Luke Hunter James-Erickson
    * [GitHub](https://github.com/LHJE)
    * [LinkedIn](https://www.linkedin.com/in/luke-hunter-james-erickson-b65682143/)
  * Nico Rithner
    * [GitHub](https://github.com/nicorithner)
    * [LinkedIn](https://www.linkedin.com/in/nicorithner/)
  * Norma Lopez
    * [GitHub](https://github.com/IamNorma)
    * [LinkedIn](https://www.linkedin.com/in/norma-lopez/)
  * Roberto Rodriguez
    * [GitHub](https://github.com/robertorodriguez12)
    * [LinkedIn](https://www.linkedin.com/in/roberto-j-rodriguez12/)
