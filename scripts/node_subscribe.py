#! /usr/bin/env python3

import time
import rospy
import std_msgs.msg

def callback(req):
    pass
    return

if __name__=="__main__":
    rospy.init_node("subscriber")
    num = rospy.get_param("~n")

    topic_from = rospy.Subscriber(
            name = "node_check{}".format(num),
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
