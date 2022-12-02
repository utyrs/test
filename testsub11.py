#!/usr/bin/env python

import rospy
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point


def callback(data):
    x = data.markers[0].pose.position.x
    #rospy.loginfo(rospy.get_caller_id() + 'I heard' + str(data.markers[0].pose.position.x))
    print(str(x))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/visualization/planning/planner_visualization', MarkerArray, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()

