#! /usr/bin/env python3

name = "topic_subscriber_number"

import sys
import time
import threading
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite


def callback1(req):
    time_sub = time.time()
    
    print(time_sub, req.data)
    time_hensa = time_sub - req.data
    
    n.write("topic_number", '', (time_hensa, time_sub), auto_commit=True)
    return

def callback(req):
    time_sub = time.time()
    
    #print(time_sub, req.data)
    time_hensa = time_sub - req.data
    
    #n.write("topic_number", '', (time_hensa, time_sub), auto_commit=True)
    return

if __name__=="__main__":
    rospy.init_node(name)
    n = n2lite.N2lite("/home/amigos/data/topic_speed/topic_number1.db")

    n.make_table("topic_number", "(dif float, time float)")

    topic1 = rospy.Subscriber(
            name = "topic_check_number1",
            data_class = std_msgs.msg.Float64,
            callback = callback1,
            queue_size = 1,
            )

    topic_from = [rospy.Subscriber(
            name = "topic_check_number{}".format(i),
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            ) for i in range(2, 101)]

    rospy.spin()
