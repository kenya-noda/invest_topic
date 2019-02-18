#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite


def callback(req):
    time_sub = time.time()
    
    time_hensa = time_sub - req.data
    return

if __name__=="__main__":
    rospy.init_node("sub_ex")
    num = rospy.get_param("~n")

    topic_from = rospy.Subscriber(
            name = "node_check{}".format(num),
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
