#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Polygon
from geometry_msgs.msg import Point32

dimensions = {
    "wheelbase": 0.3302,
    "width": 0.2032,
    "height": 0.1,
    "ground_offset": 0.04,
    "wheel_radius": 0.0508,
    "wheel_length": 0.0381,
    "laser_distance_from_base_link": 0.275,
    "laser_height": 0.05,
    "laser_radius": 0.026,
}

wheelbase = dimensions["wheelbase"]
width = dimensions["width"]
wheel_radius = dimensions["wheel_radius"]
wheel_length = dimensions["wheel_length"]


def publish_footprint():
    rospy.init_node('footprint')
    pub = rospy.Publisher('/costmap/footprint', Polygon, queue_size=10)

    full_width = width + wheel_length
    msg = Polygon([
        # back-left, back-right, front-left, front-right
        Point32(-wheel_radius,             -full_width, 0),
        Point32(-wheel_radius,              full_width, 0),
        Point32( wheel_radius + wheelbase, -full_width, 0),
        Point32( wheel_radius + wheelbase,  full_width, 0),
    ])

    rate = rospy.Rate(60)
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    publish_footprint()
