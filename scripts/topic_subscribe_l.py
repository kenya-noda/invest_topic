#! /usr/bin/env python3

name = "topic_subscriber_l"

import sys
import time
import threading
import rospy
import std_msgs.msg

d = "/home/amigos/data/"

def callback(req, num):
    try:
        time_sub = time.time()
        f = open(d + "topic_check{}.txt".format(num), "a")
    
        print(time_sub, req.data)
        time_hensa = str(time_sub - req.data)

        f.write(time_hensa + "\n")
        f.close()
    except KeyBoardInterrupt:
        f.close()
        sys.exit(-1)
    return

if __name__=="__main__":
    rospy.init_node(name)
    num = rospy.get_param("~num")

    topic_from = rospy.Subscriber(
            name = "topic_check",
            data_class = std_msgs.msg.Float64,
            callback = callback,
            callback_args = num,
            queue_size = 1,
            )

    rospy.spin()
