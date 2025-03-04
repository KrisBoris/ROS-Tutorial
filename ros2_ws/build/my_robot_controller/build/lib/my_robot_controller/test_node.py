#!/usr/bin/env python3
import rclpy as ros
from rclpy.node import Node
# interpreter line to tell the interpreter to use pyhon3


class MyNode(Node):

    def __init__(self):
        # pass ndoes name
        super().__init__("test_node")
        # write a message to logger
        self.get_logger().info("Hello there from ROS")


def main(args=None):
    # start ROS communication
    ros.init(args=args)
    
    node = MyNode()

    # run node in loop until it's killed (by e.g. Ctrl+C)
    ros.spin(node)

    # shutdown ROS communication
    ros.shutdown()

if __name__ == '__main__':
    main()