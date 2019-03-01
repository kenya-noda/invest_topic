#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node("publisher")
    num = int(rospy.get_param("~n"))
    n_node = int(rospy.get_param("~n_node"))
    byt = ["1"]*8
    st = "".join(byt)

    topic_to = [rospy.Publisher(
            name = "node_check{0}_{1}".format(n_node, i),
            data_class = std_msgs.msg.String,
            queue_size = 1,
            )for i in range(1, num+1)]

    while not rospy.is_shutdown():
        [topic.publish(st) for topic in topic_to]
        time.sleep(0.1)
        continue
