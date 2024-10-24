import rclpy
from rclpy.node import Node
from ros_tcp_endpoint import TcpServer

from matsive_r2msgs.msg import UnityCubePosition
from moveit_msgs.msg import RobotTrajectory
from std_msgs.msg import String

import sys
import numpy as np
import time


class PositionSubscriber(Node):

    def __init__(self):
        super().__init__('position_subscriber')
        self.subscription = self.create_subscription(
            UnityCubePosition,
            '/CubePos',
            self.listener_callback,
            10
        )
        self.subscription  # Prevent unused variable warning
        self.received_data = None  # Initialize a variable to store the received data

    def listener_callback(self, data):
        self.received_data = data  # Store the received message in the class variable
        #self.get_logger().info(f'{data}')  # Optional: Log the received data


def main(args=None):
    rclpy.init(args=args)
   
    tcp_server = TcpServer("UnityEndpoint")
    tcp_server.start()
    position_subscriber = PositionSubscriber()   
    
    try:
        while rclpy.ok():
            rclpy.spin_once(position_subscriber,timeout_sec=0.1)  # Process incoming messages
            if position_subscriber.received_data is not None:
            
                x_value = position_subscriber.received_data.x[0]  # Extract the first element from each array
                y_value = position_subscriber.received_data.y[0]
                z_value = position_subscriber.received_data.z[0]
                q1_value = position_subscriber.received_data.q1[0]
                q2_value = position_subscriber.received_data.q2[0]
                q3_value = position_subscriber.received_data.q3[0]
                #print(f'{position_subscriber.received_data}')
                print(f"x: {x_value}, y: {y_value}, z: {z_value}, q1: {q1_value}, q2: {q2_value}, q3: {q3_value}")
            #time.sleep(0.1)
    except KeyboardInterrupt:
        pass  # Handle keyboard interrupt for graceful shutdown

    # Destroy the node explicitly
    position_subscriber.destroy_node()
    rclpy.shutdown()
    tcp_server.setup_executor()
    tcp_server.destroy_nodes()
    rclpy.shutdown()
    robot_shutdown()


if __name__ == "__main__":
    main()

