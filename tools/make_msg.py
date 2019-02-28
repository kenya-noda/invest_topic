#!/usr/bin/env python3

import subprocess
import time

cmd = "python process-msg.py --node_num {0} --topic_num {1} --msg {2}"
node_list = [10, 40, 70, 100]
topic_list = [1, 2, 6, 10, 14, 18, 20]
msg_list = ["1", "12345678", "1234567890123456"]

for node in node_list:
    for topic in topic_list:
        for msg in msg_list:
            run_cmd = cmd.format(node, topic, msg)
            run = subprocess.check_call(run_cmd.split())
            print(run_cmd, run)
