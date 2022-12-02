#!/usr/bin/env python

import rospy
from visualization_msgs.msg import MarkerArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s' + str(data.data))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/clock", Clock, callback)
    rospy.spin


if __name__ == '__main__':
    listener()
