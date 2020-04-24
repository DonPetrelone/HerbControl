# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# this function measures air temperature and humidity thorugh the AdafruitDHT 22 sensor

import sys
import Adafruit_DHT

def airTempHum (sensor, port):
    
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, port)
    
    #convert temperature to Fahrenheit
    temperature = temperature * 9/5.0 + 32
    
    #returns a tuple
    return (temperature, humidity)
