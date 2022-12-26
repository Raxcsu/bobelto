#!/usr/bin/env python
import numpy as np
import rospy
import cv2
import sys
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

br=CvBridge()
cap=cv2.VideoCapture(0)
#cap1=cv2.VideoCapture(0)
#cap.set(3,600)
#cap.set(4,450)
#cap.set(5,15)
def talker():

    pub=rospy.Publisher('video_topic',Image,queue_size=10)
    rospy.init_node('videotr',anonymous = True)
    while not rospy.is_shutdown():
        ret, img = cap.read()
        #resize_image = cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        pub.publish(br.cv2_to_imgmsg(img_gray,"mono8"))
        #print(img_gray.shape)
        #cv2.imshow("frame",img_gray)
        #cv2.imshow("frame1",frame1)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        talker()
        #cap.release()
        #cv2.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
