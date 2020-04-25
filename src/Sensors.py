# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# this files takes measurements from the sensors and stores them in DB;
# it also sends out text messages in case of any out of range measurements

import AirTempHum
import SoilMoisture
import TextMessage
import Database

#watchdog variable - always set to 1 after this file is run
global watchdog
watchdog = 1

#measured values
temp = 0
hum = 0
soil = 0

#this variable determines the type of sensor. Change to 11 if you're using it.
airSensor = 22

#Port in the raspberry pi
airPort = 4

#Channel of the microchip the soil sensor is connect to.
#Change it if you change where it is connected.
soilChannel = 0

#get temperature and humidity from temp, humidity sensors
temp, hum = AirTempHum.airTempHum(airSensor, airPort)

#get soil moisture from sensor - not being taken right now
SoilMoisture.getSoil(soilChannel)

#store values in the DB
Database.dbInsert(temp,hum,soil)

#getting ranges from DB, checking ranges and warning user via text message.
airTempHighDanger, airTempHighWarning, airTempGood, airTempLowWarning, airTempLowDanger, airHumHighDanger, \
airHumHighWarning, airHumGood, airHumLowWarning, airHumLowDanger, soilMoistHighDanger, soilMoistHighWarning, \
soilMoistGood, soilMoistLowWarning, soilMoistLowDanger = Database.dbGetRanges()

if hum is not None and temp is not None and soil is not None:
    if temp >= airTempHighDanger:
        TextMessage.text("Danger - Air Temperature High")
    elif airTempHighWarning <= temp < airTempHighDanger:
        TextMessage.text("Warning - Air Temperature High")
    elif airTempLowDanger < temp <= airTempLowWarning:
        TextMessage.text("Warning - Air Temperature Low")
    elif temp <= airTempLowDanger:
        TextMessage.text("Danger - Air Temperature Low")

    if hum >= airHumHighDanger:
        TextMessage.text("Danger - Air Humidity High")
    elif airHumHighWarning <= hum < airHumHighDanger:
        TextMessage.text("Warning - Air Humidity High")
    elif airHumLowDanger < hum <= airHumLowWarning:
        TextMessage.text("Warning - Air Humidity Low")
    elif hum <= airHumLowDanger:
        TextMessage.text("Danger - Air Humidity Low")

    if soil >= soilMoistHighDanger:
        TextMessage.text("Danger - Soil Moisture High")
    elif soilMoistHighWarning <= soil < soilMoistHighDanger:
        TextMessage.text("Warning - Soil Moisture High")
    elif soilMoistLowDanger < soil <= soilMoistLowWarning:
        TextMessage.text("Warning - Soil Moisture Low")
    elif soil <= soilMoistLowDanger:
        TextMessage.text("Danger - Soil Moisture Low")
else:
    #in case any measurements were not taken - warn user
    TextMessage.text("Measurements not taken")

#fucntion to get the watchdog variable
def getWatchdog():
    return watchdog
