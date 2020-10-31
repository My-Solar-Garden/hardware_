from time import sleep # we need to use the sleep function to delay readings
import datetime # that's for printing the current date
import time
import grovepi
import math
import json
import requests
import sys
# import code #this is like require pry
# code.interact(local=dict(globals(), **locals())) #this is like binding pry
print('-------------------------------')
print("Let's insert your sensor IDs")

sensors = ['Light', 'Temperature & Humidity']
sensor_ids = dict()

for sensor in sensors:
    answer = None
    id = None
    while answer != "Y" and answer != "N":
        print("Do you have a % s sensor? [Y/N]" % sensor)
        answer = raw_input().upper()

        if answer == "Y":
            while not isinstance(id, int):
                print("\nPlease enter the % s ID as shown on the My Sensors page in your My Solar App" % sensor)
                print("% s ID: " % sensor)
                id = int(input())

            sensor_ids[sensor] = id

dht_sensor = 2      # port D2
light_sensor = 0    # port A0
ledbar = 4          # port D4

val = 0

# grovepi.additional_waiting = 0.005
grovepi.pinMode(dht_sensor,"INPUT")
grovepi.pinMode(light_sensor,"INPUT")
grovepi.ledBar_init(ledbar, 0)

data = {
    'light': 0,
    'temp': 0,
    'humidity': 0,
    'ir': 3 * [0]
}

while True:
    if sensor_ids.has_key('Light'):
        data['light'] = grovepi.analogRead(light_sensor)
        requests.post("https://solar-garden-be.herokuapp.com/api/v1/garden_healths", params={'sensor_id': sensor_ids['Light'], 'reading_type': 'light', 'reading': data['light']})

    if sensor_ids.has_key('Temperature & Humidity'):
	      data['temp'],data['humidity'] = grovepi.dht(dht_sensor,0)
        requests.post("https://solar-garden-be.herokuapp.com/api/v1/garden_healths", params={'sensor_id': sensor_ids['Temperature & Humidity'], 'reading_type': 'temperature', 'reading': data['temp']})

    grovepi.ledBar_setBits(ledbar, val % 1024)
    val += 1
    print(json.dumps(data))
    time.sleep(2)
