#! /usr/bin/env python3

name = "topic_multi_publisher"

import time
import rospy
import std_msgs.msg

numbers = [i for i in range(10)]

if __name__=="__main__":
    rospy.init_node(name)

    topic_to = [rospy.Publisher(
            name = "topic_check_{}".format(num),
            data_class = std_msgs.msg.Float64,
            queue_size = 1,
            ) for num in numbers]
    
    while not rospy.is_shutdown():

        for pub in topic_to:
            t = time.time()
            print(t)
            
            pub.publish(t)

        time.sleep(0.01)
        continue
