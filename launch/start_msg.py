#!/usr/bin/env python3

import subprocess
import time

cmd = "roslaunch msg{0}_{1}_{2}.launch"
node_list = [10, 40, 70, 100]
topic_list = [1, 2, 6, 10, 14, 18, 20]
msg_byte = [16]
msg_list = ["1234567890123456"]

for (i, msg) in zip(msg_byte, msg_list):
    for node in node_list:
        for topic in topic_list:
            run_cmd = cmd.format(node, topic, msg)
            run = subprocess.check_call(run_cmd.split())
            print(run_cmd, run)
            time.sleep(5)
