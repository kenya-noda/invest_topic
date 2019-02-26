#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse

p = argparse.ArgumentParser()
p.add_argument("--node_num", type=int)
p.add_argument("--topic_num", type=int)
args = p.parse_args()

node_num = args.node_num
topic_num = args.topic_num


launch = ET.Element("launch")
tree = ET.ElementTree(element=launch)

ET.SubElement(launch, "node",
        {"name":"p0", "type":"node_saver_p.py", "pkg":"invest_topic"}
        )

ET.SubElement(launch, "node",
        {"name":"s0", "type":"node_saver_s.py", "pkg":"invest_topic"}
        )

for i in range(1, node_num+1):
    node_p = ET.SubElement(launch, "node",
            {"name":"p{}".format(i), "type":"process_publish.py", "pkg":"invest_topic"}
            )
    ET.SubElement(node_p, "param",
            {"name":"n_node", "value":"{}".format(i)}
            )
    ET.SubElement(node_p, "param",
            {"name":"n", "value":"{}".format(topic_num)}
            )

    node_s = ET.SubElement(launch, "node",
            {"name":"s{}".format(i), "type":"process_subscribe.py", "pkg":"invest_topic"}
            )
    ET.SubElement(node_s, "param",
            {"name":"n_node", "value":"{}".format(i)}
            )
    ET.SubElement(node_s, "param",
            {"name":"n", "value":"{}".format(topic_num)}
            )

tree.write("test.launch", encoding="utf-8")
#tree.write("/home/amigos/ros/src/invest_topic/launch/thread{0}_{1}.launch".format(node_num, topic_num), encoding="utf-8")
