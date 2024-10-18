# ROS2 Section
[Go To Main Page
](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Part%201.%20Installing%20of%20ROS2%20Humble.md)
## Part 2. Building ROS2 Message Package
The steps of building a package of ROS2 can be found [Here](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

Or follow the below steps:
In the example we will be generating messages from unity of a objects x,y,z position and x,y,z rotation data. For that a ROS2 msgs package will be created. This package will act as our publisher or publisher helper.
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
4. Create a package (CMake/C#). I have nameed the package `matsive_r2msg` and the following lines would come up in terminal as given in image.
   ```
   ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>
   ```
   ![image](https://github.com/user-attachments/assets/bc8e46b9-34b1-4a92-ae00-b1086fed74df)

5. Go to the created package folder open `CMakeLists.txt` to add the code below.
   (These packages should be installed with ROS2 some might need to be install)
   ```
   cmake_minimum_required(VERSION 3.8)
   project(matsive_r2msgs)

   if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
   add_compile_options(-Wall -Wextra -Wpedantic)
   endif()
   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(std_msgs REQUIRED)
   find_package(action_msgs REQUIRED)
   find_package(geometry_msgs REQUIRED)
   find_package(trajectory_msgs REQUIRED)
   find_package(moveit_msgs REQUIRED)
   find_package(sensor_msgs REQUIRED)
   find_package(rosidl_default_generators REQUIRED)
   rosidl_generate_interfaces(${PROJECT_NAME}
   "msg/UnityCubePosition.msg"
   DEPENDENCIES std_msgs geometry_msgs sensor_msgs moveit_msgs
   )
   ament_export_dependencies(rosidl_default_runtime)
   ament_package()
   ```
6. Open package.xml file to add the code below:
   ```
   <?xml version="1.0"?>
   <?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
   <package format="3">
    <name>matsive_r2msgs</name>
    <version>0.0.0</version>
    <description>TODO: Package description</description>
    <maintainer email="matsive@todo.todo">matsive</maintainer>
    <license>Apache-2.0</license>

    <buildtool_depend>ament_cmake</buildtool_depend>zn 
    <depend>rclcpp</depend>
    <depend>std_msgs</depend>
    <depend>action_msgs</depend>
    <depend>geometry_msgs</depend>
    <depend>rosidl_default_generators</depend>
    <buildtool_depend>rosidl_default_generators</buildtool_depend>
    <exec_depend>rosidl_default_runtime</exec_depend>
    <member_of_group>rosidl_interface_packages</member_of_group>
    <test_depend>ament_lint_auto</test_depend>
    <test_depend>ament_lint_common</test_depend>
    <export>
      <build_type>ament_cmake</build_type>
    </export>
   </package>
   ```
7. Then create a folder in the the package folder called `msg`. Open the `msg` folder to create a text file called `UnityCubePosition.txt` later change the extention to `.msg` or `UnityCubePosition.msg`. And add the following lines
   ```
   float64 x
   float64 y
   float64 z
   float64 rotx
   float64 roty
   float64 rotz
   ```
8. Go back to ros_ws folder
   ```
   cd ~/ros2_ws
   ```
9. To build the package which will also install the package into ros2->install directory. Replaced package name as `matsive_r2msgs`.
   ```
   colcon build --packages-select my_package
   ```
10. Now `matsive_r2msgs` can be found in ros_ws->install folder.

Proceed to [Part 3. Building ROS2 package](https://github.com/matsive/Unity_Robotics_ROS2/edit/main/Documentation/ROS2%20Section/Part%203.%20Building%20ROS2%20package.md)
