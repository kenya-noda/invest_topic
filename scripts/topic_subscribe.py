#! /usr/bin/env python3

name = "topic_subscriber"

import sys
import time
import threading
import rospy
import std_msgs.msg


def callback(req):
    try:
        f = open("topic_check.txt", "a")
    
        time_sub = time.time()
        time_hensa = str(time_sub - req.data)

        f.write(time_hensa + "\n")
        f.close()
    except KeyBoardInterrupt:
        f.close()
        sys.exit(-1)
    return

if __name__=="__main__":
    rospy.init_node(name)

    
    topic_from = rospy.Subscriber(
            name = "topic_check",
            data_class = std_msgs.msg.Float32,
            callback = callback
            queue_size = 1,
            )

    rospy.spin()
