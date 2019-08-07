#!/usr/bin/env python
from __future__ import print_function

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_show:

  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("left_image",Image,self.left_callback)
    self.image2_sub = rospy.Subscriber("right_image",Image,self.right_callback)
    self.right_image=0
    self.left_image=0
  def left_callback(self,data):
    try:
      self.left_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      # print ("here")
    except CvBridgeError as e:
      print(e)
    # print (self.left_image)
    cv2.imshow("left_image", self.left_image)
    cv2.imshow("right_image", self.right_image)
    cv2.waitKey(3)

  def right_callback(self,data):
    try:
      self.right_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      # print ("here")
    except CvBridgeError as e:
      print(e)

def main():
  C = image_show()
  rospy.init_node('image_show', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
