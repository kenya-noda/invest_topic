#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node("publisher")

    topic_to = rospy.Publisher(
            name = "node_check0",
            data_class = std_msgs.msg.Float64,
            queue_size = 1,
            )

    time.sleep(10)

    while not rospy.is_shutdown():
        t = time.time()
        topic_to.publish(t)
        time.sleep(0.1)
        continue
