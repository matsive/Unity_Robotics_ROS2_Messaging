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
4. Create a package (Python). I have nameed the package `matsive_r2` and the following lines would come up in terminal as given in image.
   ```
   ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
   ```
After running the following lines should be seen in terminal 
`going to create a new package
package name: my_package
destination directory: /home/user/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['<name> <email>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
node_name: my_node
creating folder ./my_package
creating ./my_package/package.xml
creating source folder
creating folder ./my_package/my_package
creating ./my_package/setup.py
creating ./my_package/setup.cfg
creating folder ./my_package/resource
creating ./my_package/resource/my_package
creating ./my_package/my_package/__init__.py
creating folder ./my_package/test
creating ./my_package/test/test_copyright.py
creating ./my_package/test/test_flake8.py
creating ./my_package/test/test_pep257.py
creating ./my_package/my_package/my_node.py`



