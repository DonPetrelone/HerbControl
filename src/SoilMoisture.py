import spidev
import os
import time

spi = spidev.SpiDev()
spi.open(0,0)

def getSoil(channel):
	val = spi.xfer2([1,(8+channel)<<4,0])
	data = ((val[1]&3) << 8) + val[2]
	return data
