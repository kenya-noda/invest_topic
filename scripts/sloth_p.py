#! /usr/bin/env python3

import time
import rospy


if __name__=="__main__":
    rospy.init_node("publisher")
    while not rospy.is_shutdown():
        time.sleep(0.1)
        continue
