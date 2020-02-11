#Herb Control - Senior Design Project
#Western Michigan University
#Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
#Faculty Advisor: Dr. John Kapenga
#This is the main file of the program

import AirTempHum
import TextMessage
import VoltageControl

temp = 0
hum = 0
airSensor = 22
airPort = 4
lightPin = 7


temp, hum = AirTempHum.airTempHum(airSensor, airPort)

if hum is not None and temp is not None:
    TextMessage.text("Fuck")    
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temp, hum))
else:
    print('Failed to get reading. Try again!')

#VoltageControl.pinVoltage(lightPin, 1, 0)