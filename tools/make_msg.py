#!/usr/bin/env python3

import subprocess
import time

cmd = "python process-msg.py --node_num {0} --topic_num {1} --msg {2}"
node_list = [10, 20, 40, 60, 80, 100]
topic_list = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
msg_list = ["1", "12345678", "1234567890123456", "12345678901234567890123456789012", "1234567890123456789012345678901234567890123456789012345678901234"]

for node in node_list:
    for topic in topic_list:
        for msg in msg_list:
            run_cmd = cmd.format(node, topic, msg)
            run = subprocess.check_call(run_cmd.split())
            print(run_cmd, run)
