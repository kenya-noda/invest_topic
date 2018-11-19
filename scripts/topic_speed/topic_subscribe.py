#! /usr/bin/env python3

name = "topic_subscriber"

import sys
import time
import threading
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite


def callback(req):
    time_sub = time.time()
    
    print(time_sub, req.data)
    time_hensa = time_sub - req.data
    
    n.write("topic_speed", '', (time_hensa, time_sub), auto_commit=True)
    return

if __name__=="__main__":
    rospy.init_node(name)
    n = n2lite.N2lite("/home/amigos/data/topic_speed/topic_speed.db")

    n.make_table("topic_speed", "(dif float, time float)")

    topic_from = rospy.Subscriber(
            name = "topic_check",
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
