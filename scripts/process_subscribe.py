#! /usr/bin/env python3

import time
import rospy
import std_msgs.msg

def callback(req):
    pass
    return

if __name__=="__main__":
    rospy.init_node("subscriber")
    num = int(rospy.get_param("~n"))
    n_node = int(rospy.get_param("~n_node"))

    topic_from = [rospy.Subscriber(
            name = "node_check{0}_{1}".format(n_node, i),
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            ) for i in range(1, num+1)]

    rospy.spin()
