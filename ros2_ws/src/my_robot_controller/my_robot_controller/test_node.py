#!/usr/bin/env python3
import rclpy as ros
from rclpy.node import Node
# interpreter line to tell the interpreter to use pyhon3


class MyNode(Node):

    def __init__(self):
        # pass ndoes name
        super().__init__("test_node")
        self.counter = 0
        # write a message to logger
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello there from ROS tutorial: " + str(self.counter))
        self.counter += 1


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