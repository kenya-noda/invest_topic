#!/usr/bin/env python3

import subprocess
import time

cmd = "roslaunch msg{0}_{1}.launch"
node_list = [10, 20, 40, 60, 80, 100]
topic_list = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
msg_byte = [1, 8, 16, 32, 64]

cmd_end = "mv node_number* msg_{}"

for msg in msg_byte:
    for node in node_list:
        for topic in topic_list:
            run_cmd = cmd.format(node, topic)
            run = subprocess.check_call(run_cmd.split())
            print(run_cmd, run)
            time.sleep(5)

    run_cmd2 = cmd_end.format(msg)
    run2 = subprocess.check_call(run_cmd2.split())

