#! /usr/bin/env python3

name = "topic_publisher_number"

import time
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node(name)

    topic_to = []
    i = 0
    while i != 100:
        i += 1
        
        _topic_to = rospy.Publisher(
                name = "topic_check_number{}".format(i),
                data_class = std_msgs.msg.Float64,
                queue_size = 1,
                )
        topic_to.append(_topic_to)
        
        for j in range(i):
            t = time.time()
            topic_to[j].publish(t)

        print(t,i)
        time.sleep(1)
        continue
