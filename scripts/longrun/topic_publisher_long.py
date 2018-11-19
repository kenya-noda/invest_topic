#! /usr/bin/env python3

name = "topic_publisher_long"

import time
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node(name)

    topic_to = rospy.Publisher(
            name = "topic_check_long",
            data_class = std_msgs.msg.Float64,
            queue_size = 1,
            )
    i = 0
    while i != 144:
        t = time.time()
        print(t, i)
        topic_to.publish(t)
        i += 1
        time.sleep(1800)
        continue
