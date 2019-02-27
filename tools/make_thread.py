#!/usr/bin/env python3

import subprocess
import time

cmd = "python thread.py --node_num {0} --topic_num {1}"
node_list = [10, 20, 40, 60, 80, 100]
topic_list = [10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

for node in node_list:
    for topic in topic_list:
        run_cmd = cmd.format(node, topic)
        run = subprocess.check_call(run_cmd.split())
        print(run_cmd, run)
