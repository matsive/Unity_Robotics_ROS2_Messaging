# ROS2 Section
[Go To Main Page
](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Part%201.%20Installing%20of%20ROS2%20Humble.md)
## Part 3. Building ROS2 package 
The steps of building a package of ROS2 can be found [Here](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

Or follow the below steps:
To subcribe or listen to the messages from unity we can check all the nodes available in the local network and select which one we want to listen to or we can create a package to receive the messages.
1. Source ROS2
   ```
   source /opt/ros/humble/setup.bash
   ```
2. Check ROS2 version
   ```
   echo $ROS_DISTRO
   ```
3. Go to ros2_ws -> src folder
   ```
   cd ~/ros2_ws/src
   ```
4. Create a package (Python). I have nameed the package `matsive_r2`.
   ```
   ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
   ```  
5. After creating package, inside the package folder there should be a folder with the same name aka `matsive_r2` for this case. Now create a python file named `Connect_Unity.py` and add the following code.
   ```
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
           self.received_data = data.joints  # Store the received message in the class variable
           #self.get_logger().info(f'{data}')  # Optional: Log the received data


   def main(args=None):
       rclpy.init(args=args)
       sys.exit()
       tcp_server = TcpServer("UnityEndpoint")
       tcp_server.start()
       trajectory_subscriber = TrajectorySubscriber()   
       try:
       while rclpy.ok():
            rclpy.spin_once(position_subscriber,timeout_sec=0.1)  # Process incoming messages
            if position_subscriber.received_data is not None:
                print(f'{position_subscriber.received_data}')
   
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
   ```
6. Edit `package.xml` in package folder and add the following code. This should include the packages required to run the the python code.
   ```   
   <?xml version="1.0"?>
   <?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
   <package format="3">
    <name>matsive_r2</name>
    <version>0.0.0</version>
    <description>TODO: Package description</description>
    <maintainer email="matsive@todo.todo">matsive</maintainer>
    <license>Apache-2.0</license>
    <buildtool_depend>ament_python</buildtool_depend>
    <depend>rclpy</depend>
    <depend>ros_tcp_endpoint</depend>
    <depend>moveit_msgs.msg</depend>
    <test_depend>ament_copyright</test_depend>
    <test_depend>ament_flake8</test_depend>
    <test_depend>ament_pep257</test_depend>
    <test_depend>python3-pytest</test_depend>
 
    <export>
      <build_type>ament_python</build_type>
    </export>
   </package>
   ```
7. Edit `setup.py` to add the following code. The python code `Connect_Unity.py` can be added to the ros2 package as a run command with a nicknames or shortform aka `ConnectUnity` in this case. (can also add launch comamnds slightly differently). Through this the python codes can be called using `ros2 run matsive_r2 ConnectUnity`.
   ```
   import os
   from glob import glob
   from setuptools import find_packages, setup

   package_name = 'matsive_r2'

   setup(
       name=package_name,
       version='0.0.0',
       packages=find_packages(exclude=['test']),
       data_files=[
           ('share/ament_index/resource_index/packages',
               ['resource/' + package_name]),
           ('share/' + package_name, ['package.xml']),
       ],
       install_requires=['setuptools'],
       zip_safe=True,
       maintainer='matsive',
       maintainer_email='matsive@todo.todo',
       description='TODO: Package description',
       license='Apache-2.0',
       tests_require=['pytest'],
       entry_points={
           'console_scripts': [
           'ConnectUnity = matsive_r2.Connect_Unity:main'
           ],
       },
   )
   ```
8. Go back to ros_ws folder
   ```
   cd ~/ros2_ws
   ```
9. To build the package which will also install the package into ros2->install directory. Replaced `my_package` name as `matsive_r2`.
   ```
   colcon build --packages-select my_package
   ```
10. Now `matsive_r2` can be found in ros_ws->install folder. Also it can be run using `ros2 run matsive_r2 ConnectUnity`.

Proceed to [Part 4. Install Unity Hub](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/Unity%20Section/Part%204.%20Install%20Unity%20Hub.md)



