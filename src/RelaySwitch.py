# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# this is the file that sends voltage to the realy switch and controls the lights and heating mat.

import VoltageControl
import sys

lightPin = 7
voltage = int(sys.argv[1])
inOut = 1

VoltageControl.pinVoltage(lightPin, inOut, voltage)
