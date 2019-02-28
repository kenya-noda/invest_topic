#! /usr/bin/env python3

import time
import rospy
import std_msgs.msg


def callback(req):
    topic_to.publish(req.data)
    return

if __name__=="__main__":
    rospy.init_node("returner")

    topic_to = rospy.Publisher(
            name = "node_check0",
            data_class = std_msgs.msg.Float64,
            queue_size = 1,
            )

    topic_from = rospy.Subscriber(
            name = "node_check",
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
