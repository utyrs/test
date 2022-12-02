#!/usr/bin/env python

import rospy
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard' + str(data.markers[0].pose))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/visualization/planning/planner_visualization', MarkerArray, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()

