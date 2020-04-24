# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# this method switches the voltage output of a desired pin.

import wiringpi
import time

def pinVoltage (pin, inOut, highLow):
    
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(pin, inOut)
    wiringpi.digitalWrite(pin,highLow)
        
    return
    
