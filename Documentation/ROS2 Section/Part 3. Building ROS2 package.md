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
# finish editing below please   
5. After creating package inside the package there should be a folder with the same name aka `matsive_r2` for this case. Now create a python file named `xxx` and add the following code.
   ```
   xxx
   ```
6. Edit `package.xml` and add the following code. This should include the packages required to run the the python code.
   ```
   xxx
   ```
7. Edit `setup.py` to add the following code. The python code `xxx` can be added to the ros2 package as a run command with a nicknames or shortform aka `xxxxx` in this case. (can also add launch comamnds slightly differently). Through this the python codes can be called using `ros2 run matsive_r2 xxxxx`.
   ```
   xx
   ```
8. Go back to ros_ws folder
   ```
   cd ~/ros2_ws
   ```
9. To build the package which will also install the package into ros2->install directory. Replaced `my_package` name as `matsive_r2`.
   ```
   colcon build --packages-select my_package
   ```
10. Now `matsive_r2` can be found in ros_ws->install folder. Also it can be run using `ros2 run matsive_r2 xxxxx`.

Proceed to



