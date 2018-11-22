#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite

args = sys.argv
name = "node_subscriber{}".format(args[1])


def callback(req):
    time_sub = time.time()
    
    time_hensa = time_sub - req.data
    
    n.write("node_number{}".format(args[1]), '', (time_hensa, time_sub), auto_commit=True)
    return

if __name__=="__main__":
    rospy.init_node(name)
    n = n2lite.N2lite("/home/amigos/data/multi_publisher/node_number.db")

    n.make_table("node_number{}".format(args[1]), "(dif float, time float)")

    topic_from = rospy.Subscriber(
            name = "node_check",
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
