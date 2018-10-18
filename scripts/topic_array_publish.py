#! /usr/bin/env python3

name = "array_publisher"

import time
import numpy
import rospy
import std_msgs.msg


if __name__=="__main__":
    rospy.init_node(name)

    topic_to = rospy.Publisher(
            name = "array_check",
            data_class = std_msgs.msg.Float64MultiArray,
            queue_size = 1,
            )
    
    while not rospy.is_shutdown():
        array = std_msgs.msg.Float64MultiArray()
        array.data = numpy.array([[time.time(), 1.0],[time.time(), 2.0]])
        print(array)
        topic_to.publish(array)
        time.sleep(1)
        continue
