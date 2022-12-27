



import serial
import time
import Fabu_PCA9685
import smbus as smbus

bus=smbus.SMBus(1)
PCA9685 = Fabu_PCA9685.PCA9685(bus,value=300)
PCA9685.set_hz(50)

vel_x = 0
vel_y = 0
vel_w = 0
vel_z = 0
#joy_r2	  = 0 # no se usa por ahora
#joy_r1	  = 0
#joy_l1    = 0

gain = 80
ps = 50

max=40

def interp_esc(val):

	val = 90+val
	x = (float(val)/180)
	i = 236 + int((x*165))
	#i  = 250 + (x*165)
	#x =float((val-5)/90)
	#i = 235 + int(x*165)
	print(i)
	return i

def inicio():
	#PCA9685.set_channel_value(0, interp_esc(0))
	#PCA9685.set_channel_value(1, interp_esc(0))
	#PCA9685.set_channel_value(2, interp_esc(0))
	#PCA9685.set_channel_value(3, 0)
	#PCA9685.set_channel_value(4, interp_esc(0))
	#PCA9685.set_channel_value(5, interp_esc(0))
	PCA9685.set_channel_value(6, interp_esc(0))
	#PCA9685.set_channel_value(7, 0)
	#PCA9685.set_channel_value(8, 0)
	#PCA9685.set_channel_value(9, 0)
	#PCA9685.set_channel_value(10, 0)
	#PCA9685.set_channel_value(11, 0)
	#PCA9685.set_channel_value(12, 0)
	#PCA9685.set_channel_value(13, 0)
	#PCA9685.set_channel_value(14, 0)
	#PCA9685.set_channel_value(15, 0)


inicio()
#time.sleep(7)
#PCA9685.set_channel_value(6,318)
time.sleep(7)
print("INICIO")
#inicio(45)
#inicio(0)

while True:

	q = [ 80, 80, 80, 80, 80, 80, 80]

	#PCA9685.set_channel_value(0, interp_esc(q[0]))
	#PCA9685.set_channel_value(1, interp_esc(q[1]))
	#PCA9685.set_channel_value(2, interp_esc(q[2]))
	#PCA9685.set_channel_value(4, interp_esc(q[4]))
	#PCA9685.set_channel_value(5, interp_esc(q[5]))
	PCA9685.set_channel_value(6,interp_esc(q[6]))
