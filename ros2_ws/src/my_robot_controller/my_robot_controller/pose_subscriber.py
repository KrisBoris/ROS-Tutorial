#!/usr/bin/env python3
import rclpy as ros
from rclpy.node import Node
from turtlesim.msg import Pose


class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))


def main(args=Node):
    ros.init(aegs=args)
    node = PoseSubscriberNode()
    ros.spin(node)
    ros.shutdown()