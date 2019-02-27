#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse

p = argparse.ArgumentParser()
p.add_argument("--node_num", type=int)
p.add_argument("--topic_num", type=int)
p.add_argument("--msg", type=str)
args = p.parse_args()

node_num = args.node_num
topic_num = args.topic_num
msg = args.msg


launch = ET.Element("launch")
tree = ET.ElementTree(element=launch)

ET.SubElement(launch, "machine",
        {"name":"necserver", "address":"necserver", "env-loader":"/home/amigos/ros/devel/env.sh",
            "user":"amigos", "password":"NakaY0s1"}
        )

for i in range(1, node_num+1):
    node_p = ET.SubElement(launch, "node",
            {"name":"p{}".format(i), "type":"msg_p.py", "pkg":"invest_topic"}
            )
    ET.SubElement(node_p, "param",
            {"name":"n_node", "value":"{}".format(i)}
            )
    ET.SubElement(node_p, "param",
            {"name":"n", "value":"{}".format(topic_num)}
            )
    ET.SubElement(node_p, "param",
            {"name":"msg", "value":"{}".format(msg)}
            )

    node_s = ET.SubElement(launch, "node",
            {"name":"s{}".format(i), "type":"msg_s.py", "pkg":"invest_topic", "machine":"necserver"}
            )
    ET.SubElement(node_s, "param",
            {"name":"n_node", "value":"{}".format(i)}
            )
    ET.SubElement(node_s, "param",
            {"name":"n", "value":"{}".format(topic_num)}
            )

ET.SubElement(launch, "node",
        {"name":"p0", "type":"node_saver_p.py", "pkg":"invest_topic"}
        )

save = ET.SubElement(launch, "node",
        {"name":"s0", "type":"node_saver_s.py", "pkg":"invest_topic", "output":"screen", "machine":"necst", "required":"true"}
        )
ET.SubElement(save, "param",
        {"name":"topic", "value":"{}".format(topic_num)}
        )
ET.SubElement(save, "param",
        {"name":"node", "value":"{}".format(node_num)}
        )

#tree.write("test.launch", encoding="utf-8")
tree.write("/home/amigos/ros/src/invest_topic/launch/msg{0}_{1}.launch".format(node_num, topic_num), encoding="utf-8")
