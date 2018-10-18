#! /usr/bin/env python3

name = "topic_mulit_subscriber"

import sys
import time
import threading
import rospy
import std_msgs.msg

d = "/home/amigos/data/"

numbers = [i for i in range(10)]

def callback(req, num):
    try:
        f = open(d + "topic_check_{}.txt".format(num), "a")
    
        time_sub = time.time()
        print(time_sub, req.data, num)
        time_hensa = str(time_sub - req.data)

        f.write(time_hensa + "\n")
        f.close()
        time.sleep(1+num) # for sub multi test
    except KeyBoardInterrupt:
        f.close()
        sys.exit(-1)
    return

if __name__=="__main__":
    rospy.init_node(name)

    topic_from = [rospy.Subscriber(
            name = "topic_check_{}".format(num),
            data_class = std_msgs.msg.Float64,
            callback = callback,
            callback_args = num,
            queue_size = 1,
            ) for num in numbers]

    rospy.spin()
