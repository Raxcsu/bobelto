##!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name
#import rospy
import serial
import time
#from sensor_msgs.msg import JointState
#from sensor_msgs.msg import Joy
import Fabu_PCA9685
#import time
import smbus2 as smbus

bus=smbus.SMBus(1)
PCA9685 = Fabu_PCA9685.PCA9685(bus,value=300)
PCA9685.set_hz(50)

vel_x = 0
vel_y = 0
vel_w = 0
vel_z = 0
#joy_r2	  = 0 # no se usa
#joy_r1	  = 0
#joy_l1    = 0

gain = 80
ps = 50

max=40

def callback(msg):                        # RECEPCION DEL VECTOR DE JOYSTICK
	global vel_w
	global vel_x
	global vel_y
	global vel_z
	#global joy_r2 # no se usa
	#global joy_l1
	#global joy_r1
	vel_w = msg.axes[0]
	vel_x = msg.axes[1]
	vel_y = msg.axes[3]
	vel_z = msg.axes[4]
	#joy_r2 = msg.axes[5]
	#joy_r1 = msg.buttons[5]
	#joy_l1 = msg.buttons[4]
	#print(joy_pos1X)
	#print(msg.axes)


def interp_esc(val):

	val = 90+val
	x = (float(val)/180)
	i = 235 + (x*165)
	#x =float((val-5)/90)
	#i = 235 + int(x*165)
	return i

def inicio():
	PCA9685.set_channel_value(0, interp_esc(0))
	PCA9685.set_channel_value(1, interp_esc(0))
	PCA9685.set_channel_value(2, interp_esc(0))
	#PCA9685.set_channel_value(3, interp_esc(0))
	PCA9685.set_channel_value(4, interp_esc(0))
	PCA9685.set_channel_value(5, interp_esc(0))
	PCA9685.set_channel_value(6, interp_esc(0))
	PCA9685.set_channel_value(7, 0)
	PCA9685.set_channel_value(8, 0)
	PCA9685.set_channel_value(9, 0)
	PCA9685.set_channel_value(10, 0)
	PCA9685.set_channel_value(11, 0)
	PCA9685.set_channel_value(12, 0)
	PCA9685.set_channel_value(13, 0)
	PCA9685.set_cha	



#q[2]=0



'''			#	q[4]=0
			#	q[5]=0
			#else:
			q[0] = int(round(max*(vel_z)))
			q[1] = int(round(max*((1/(vel_x + vel_y + vel_w+1e-10))*(-(vel_x**2)+(vel_y**2)+(vel_w**2)))))
			q[2] = int(round(max*((1/(vel_x + vel_y + vel_w+1e-10))*( (vel_x**2)+(vel_y**2)-(vel_w**2)))))
			q[3] = int(round(max*(vel_z)))
			q[4] = int(round(max*((1/(vel_x + vel_y + vel_w+1e-10))*(-(vel_x**2)-(vel_y**2)-(vel_w**2)))))
			q[5] = int(round(max*((1/(vel_x + vel_y + vel_w+1e-10))*( (vel_x**2)-(vel_y**2)+(vel_w**2)))))
			#q[0] =  20
			#q[5] =  int(round(20*vel_x))
			#q[2] =  20
			#q[3] =  20
			#q[4] =  20
			#q[5] =  20
			#jstate.position = q
			#pub.publish(jstate)
			print(q)
			for i in range(7):
				PCA9685.set_channel_value(i, interp_esc(q[i]))
			rate.sleep()
	except KeyboardInterrupt:
		print("KeyboardInterrupt has been caught.")

if __name__=='__main__':
	main()
'''
