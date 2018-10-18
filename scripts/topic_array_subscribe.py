#! /usr/bin/env python3

name = "array_subscriber"

import sys
import time
import threading
import numpy
import rospy
import std_msgs.msg


def callback(req):
    array = req.data
    print(array)
    print(array[0])
    print(array[:1])
    return

if __name__=="__main__":
    rospy.init_node(name)

    
    topic_from = rospy.Subscriber(
            name = "array_check",
            data_class = std_msgs.msg.Float64MultiArray,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
