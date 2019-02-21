#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite
import psutil

def callback(req):
    pass
    return

if __name__=="__main__":
    rospy.init_node("subscriber")

    topic_from = [rospy.Subscriber(
            name = "node_check{}".format(i),
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            ) for i in range(1, num+1)]

    rospy.spin()
