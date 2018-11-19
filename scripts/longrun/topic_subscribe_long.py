#! /usr/bin/env python3

name = "topic_subscriber_long"

import sys
import time
import threading
import rospy
import std_msgs.msg
sys.path.append("/home/amigos/python/n2lite/")
import n2lite

import psutil
import subprocess

args = ["ss", "-t"]

def callback(req):
    time_sub = time.time()
    
    print(time_sub, req.data)
    time_hensa = time_sub - req.data

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    pid = psutil.pids()
    pro = len(pid)
    output = subprocess.check_output(args).decode()
    soc = int(len(output.split("\n")) - 1)
    
    n.write("topic_long", '', (time_hensa, time_sub, cpu, mem, pro, soc), auto_commit=True)
    return

if __name__=="__main__":
    rospy.init_node(name)
    n = n2lite.N2lite("/home/amigos/data/topic_speed/topic_long.db")

    n.make_table("topic_long", "(dif float, time float, cpu float, memory float, process int, socket int)")

    topic_from = rospy.Subscriber(
            name = "topic_check_long",
            data_class = std_msgs.msg.Float64,
            callback = callback,
            queue_size = 1,
            )

    rospy.spin()
