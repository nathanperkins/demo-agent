#!/usr/bin/env python
"""
    Hello Python!
"""
import rospy
from gamepad import PS4Joystick
from ackermann_msgs.msg import AckermannDriveStamped

if __name__== "__main__":
    rospy.init_node('hello_python') # Resgistering node in ros master

    rospy.logwarn("Starting!")
    rate = rospy.Rate(60)
    pub = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=10)
    msg = AckermannDriveStamped()

    js = PS4Joystick()
    while not rospy.is_shutdown():
        axes, _ = js.poll()
        steer, throttle = -axes[0], (axes[5]+1)/2
        msg.drive.speed = throttle
        msg.drive.steering_angle = steer
        pub.publish(msg)
        
        rate.sleep()
        
