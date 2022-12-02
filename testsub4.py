#!/usr/bin/env python

import rospy
from visualization_msgs.msg import MarkerArray


def callback(data):
    pose = data.__getattribute__(data, "pose")
    rospy.loginfo(rospy.get_caller_id() + 'I heard' + pose.__getattribute__(pose, "position"))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/visualization/planning/planner_visualization', MarkerArray, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()

MarkerArray.get