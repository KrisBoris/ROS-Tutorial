#!/src/bin/env python3
import rclpy as ros
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial


class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Turtle controller node has started")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)   
        self.prev_x = 0     

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 0.8
            cmd.angular.z = 0.9        
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)

        if pose.x > 5.5 and self.prev_x <= 5.5:
            self.get_logger().info("Changing color to green")
            self.call_set_pen_service(0, 255, 0, 3, 0)
        elif pose.x <= 5.5 and self.prev_x > 5.5:
            self.get_logger().info("Changing color to red")
            self.call_set_pen_service(255, 0, 0, 3, 0)
        
        self.prev_x = pose.x

    def call_set_pen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().info("Waiting for service...")

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        # call_async doesn't have to wait for response
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self, future):
        try:
            # no response in this case
            response = future.result()
        except Exception as e:
            self.get_logger().error(f"Error occurred: {e}")                


def main(args=None):
    ros.init(args=args)
    node = TurtleControllerNode()
    ros.spin(node)
    ros.shutdown()