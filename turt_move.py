#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleNavigator:
    def __init__(self):
        rospy.init_node('turtle_navigator', anonymous=True)
        self.goal = [3, 3]
        self.current_pose = [0, 0, 0]
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)  # 10 Hz

    def pose_callback(self, pose_msg):
        self.current_pose = [pose_msg.x, pose_msg.y, pose_msg.theta]

    def compute_heading_angle(self):
        delta_x = self.goal[0] - self.current_pose[0]
        delta_y = self.goal[1] - self.current_pose[1]
        return math.atan2(delta_y, delta_x)

    def compute_distance_to_goal(self):
        delta_x = self.goal[0] - self.current_pose[0]
        delta_y = self.goal[1] - self.current_pose[1]
        return math.sqrt(delta_x**2 + delta_y**2)

    def run(self):
        while not rospy.is_shutdown():
            heading_angle = self.compute_heading_angle()
            distance_to_goal = self.compute_distance_to_goal()

            # Angular velocity to align with the heading angle
            angular_velocity = 1.0 * (heading_angle - self.current_pose[2])

            # Linear velocity to move towards the goal position
            linear_velocity = 0.5 * distance_to_goal

            # Limit the linear velocity to avoid sudden speed changes
            linear_velocity = min(linear_velocity, 1.0)

            # Publish velocities
            twist_msg = Twist()
            twist_msg.linear.x = linear_velocity
            twist_msg.angular.z = angular_velocity
            self.vel_pub.publish(twist_msg)

            # Check if the turtle reached the goal within a certain threshold
            if distance_to_goal < 0.5:
                rospy.loginfo("Goal reached!")
                break

            self.rate.sleep()

if __name__ == '__main__':
    try:
        navigator = TurtleNavigator()
        navigator.run()
    except rospy.ROSInterruptException:
        pass
