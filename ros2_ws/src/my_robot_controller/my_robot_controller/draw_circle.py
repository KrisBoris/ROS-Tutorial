#!/usr/bin/env python3
import rclpy as ros
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrawCircleNode(Node):
    
    def __init__(self):
        super().__init__("draw_circle_node")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(1.0, self.send_vel_cmd)
        self.get_logger().info("draw_circle_node has benn created")
    
    def send_vel_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)


def main(args=None):
    ros.init(args=args)
    node = DrawCircleNode()
    ros.spin(node)
    ros.shutdown()