#! /usr/bin/env python3

import sys
import time
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite
import psutil

def callback(req):
    time_sub = time.time()
    time_hensa = time_sub - req.data
    n.write("node_number", '', (time_hensa, time_sub), auto_commit=True)

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    nic = psutil.net_io_counters()

    n.write("status", '', (cpu, mem, nic.bytes_sent, nic.bytes_recv), auto_commit=True)
    return

if __name__=="__main__":
    rospy.init_node("subscriber")
    n = n2lite.N2lite("/home/amigos/data/multi_publisher/node_number.db")

    n.make_table("node_number", "(dif float, time float)")
    n.make_table("status", "(cpu float, mem float, send float, recv float)")

    topic_from = rospy.Subscriber(
            name = "node_check0",
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
