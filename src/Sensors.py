#Herb Control - Senior Design Project
#Western Michigan University
#Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
#Faculty Advisor: Dr. John Kapenga
#This files takes measurements from the sensors and stores them in DB;
#It also sends out text messages in case of any out of range measurements

import AirTempHum
import TextMessage

temp = 0
hum = 0
airSensor = 22
airPort = 4

'''
temp, hum = AirTempHum.airTempHum(airSensor, airPort)

if hum is not None and temp is not None:
    TextMessage.text("Fuck")    
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temp, hum))
else:
    print('Failed to get reading. Try again!')
'''