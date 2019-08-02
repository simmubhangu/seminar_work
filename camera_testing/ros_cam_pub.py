#!/usr/bin/env python

import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


rospy.init_node("stereo_mage")
left_pub = rospy.Publisher("/left_image", Image, queue_size=10)
right_pub = rospy.Publisher("/right_image",Image, queue_size=10)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
#rate = rospy.rate(10)

bridge = CvBridge()

while not rospy.is_shutdown():
	ret, frame = cap.read()
	ret1,frame1= cap2.read()
	#cv2.imshow('image',frame)
	#cv2.imshow("image2",frame1)
	left_image =bridge.cv2_to_imgmsg(frame,"bgr8")
	right_image =bridge.cv2_to_imgmsg(frame1,"bgr8")		
	left_pub.publish(left_image)
	right_pub.publish(right_image) 
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
cap.release()
cap2.release()
cv2.destroyAllWindows()
