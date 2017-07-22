#!/usr/bin/env python
# Description: The script allows to set a threshold to the light sensor.
# Author: Edward U. Benitez Rendon
# Date: 20-05-17

import paho.mqtt.client as mqtt
import time
import argparse

parser = argparse.ArgumentParser(description='Set threshold in Modules.')
parser.add_argument('board', type=int,
                    help='Specify the board to set')
parser.add_argument('value', type=int,
                    help='Threshold value')

args = parser.parse_args()
print(args.value)
print(args.board)

mqttc = mqtt.Client("thresholdSensors")
mqttc.connect("192.168.1.136", 1883)

if (args.board == 1):
	mqttc.publish("myHome/lightSensor/room01/threshold", str(args.value))