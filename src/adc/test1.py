import time

import Adafruit_ADS1x15 as ads

adc = ads.ADS1015()

while True:

	value  = adc.read_adc(0)
	#value2 = adc.read_adc(1)
	#value3 = adc.read_adc(2)
	#value4 = adc.read_adc(3)
	#print("Canal 0:  ||    canal 1   ||    canal 2    || canal 3 ")
	print(value,"             ", value2,"             " , value3,"              ", value4)
	#print(value)
	time.sleep(0.5)
