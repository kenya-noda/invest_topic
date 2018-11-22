#! /usr/bin/env python3

name = "topic_publisher"

import time
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node(name)

    topic_to = rospy.Publisher(
            name = "topic_check",
            data_class = std_msgs.msg.Float64,
            queue_size = 1,
            )
    i = 0
    while i != 1000:
        t = time.time()
        print(t)
        topic_to.publish(t)
        i += 1
        time.sleep(0.1)
        continue
