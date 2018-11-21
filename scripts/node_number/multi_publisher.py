#! /usr/bin/env python3

import subprocess
import time


if __name__=="__main__":
    
    sub = subprocess.Popen(["rosrun", "invest_topic", "node_subscribe.py", "1"])

    for i in range(1, 101):
        p = subprocess.Popen(["rosrun", "invest_topic", "node_publish.py", "{}".format(i)])
        time.sleep(1)

    time.sleep(10)
    return
