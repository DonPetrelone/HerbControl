# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga

import spidev
import os
import time

spi = spidev.SpiDev()
spi.open(0,0)

def getSoil(channel):
	val = spi.xfer2([1,(8+channel)<<4,0])
	data = ((val[1]&3) << 8) + val[2]
	return data
