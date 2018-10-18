#! /usr/bin/env python3

name = "topic_mulit_subscriber"

import sys
import time
import threading
import rospy
import std_msgs.msg

numbers = [i for i in range(10)]

def callback(req, num):
    try:
        time_sub = time.time()
        f = open("topic_check_{}.txt".format(num), "a")
    
        print(time_sub, req.data)
        time_hensa = str(time_sub - req.data)

        f.write(time_hensa + "\n")
        f.close()
        time.sleep(10) # for sub multi test
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
