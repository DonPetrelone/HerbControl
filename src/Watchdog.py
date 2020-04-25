#Herb Control - Senior Design Project
#Western Michigan University
#Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
#Faculty Advisor: Dr. John Kapenga
#This file is the watchdog for the system and works together with the
#sensors file.

import Sensors
import VoltageControl
import TextMessage
voltagePin = 7
inOut = 1
onOff = 0 #shuts everything off

#check if the watchdog is zero - case which the sensors file was not run
if Sensors.watchdog == 0:
    #send warning text message to user
    TextMessage.text("Watchdog Set - Shutting Relay Switch Off.")
    # shut everything off by calling the voltage control function
    VoltageControl.pinVoltage(voltagePin, inOut, onOff)
else:
    #change watchdog variable back to 0
    Sensors.watchdog = 0