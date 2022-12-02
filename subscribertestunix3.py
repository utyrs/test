#!/usr/bin/env python

import rospy
from rosgraph_msgs.msg import Clock

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/clock", Clock, callback)
    rospy.spin


if __name__ == '__main__':
    listener()
