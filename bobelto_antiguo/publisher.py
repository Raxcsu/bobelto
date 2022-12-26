#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name
import rospy
import serial
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
import time

q0 = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0

def callback(msg):                        # RECEPCION DEL VECTOR DE JOYSTICK

	global q0
	global q1
	global q2
	global q3
	global q4
	global q5
	q0 = msg.axes[0]
	q1 = msg.axes[1]
	q2 = msg.axes[2]
	q3 = msg.axes[3]
	q4 = msg.axes[4]
	q5 = msg.axes[5]

def main():
	rospy.init_node("joy_replublish")
	rospy.Subscriber("/joy",Joy,callback)
	pub = rospy.Publisher('/joy_rep',JointState,queue_size=1000)
	jnames = ['q0','q1','q2','q3','q4','q5']
	q = [ 0.0, 0.0, 0, 0.0, 0.0, 0]
	jstate = JointState()
	jstate.header.stamp = rospy.Time.now()
	jstate.name = jnames
	jstate.position = q
	rate = rospy.Rate(100)

	try:
		while not rospy.is_shutdown():

			jstate.header.stamp = rospy.Time.now()
			q[0] = q0
			q[1] = q1
			q[2] = q2
			q[3] = q3
			q[4] = q4
			q[5] = q5

			jstate.position = q
			pub.publish(jstate)

	except KeyboardInterrupt:
		print("KeyboardInterrupt has been caught.")

if __name__=='__main__':
	main()
