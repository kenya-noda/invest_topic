#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node("publisher")
    num = int(rospy.get_param("~n"))

    topic_to = [rospy.Publisher(
            name = "node_check{}".format(i),
            data_class = std_msgs.msg.Float64,
            queue_size = 1,
            )for i in range(1, num+1)]

    while not rospy.is_shutdown():
        t = time.time()
        [topic.publish(t) for topic in topic_to]
        time.sleep(0.1)
        continue
