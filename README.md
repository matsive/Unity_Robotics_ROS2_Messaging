# Unity_Robotics_ROS2
### Follow the main branch of this repository only
This repository demonstrates how to set up Unity-Robotics-Hub to send messages to a TCP server and subscribe to those messages using created ROS2 package. This repository is the summarization of all data/links required for it. <br />
(overall image)
# Software
- [Ubuntu 22.04.5 LTS (Jammy Jellyfish)](https://releases.ubuntu.com/jammy/)
- [Rufus](https://rufus.ie/en/)
- [Unity Hub](https://docs.unity3d.com/hub/manual/InstallHub.html#install-hub-linux)
- [Unity version 2022.3.29f1](https://unity.com/releases/editor/archive)
- [ROS2 Humble for Ubuntu](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)
# ROS2 Section Part 1 of 
[## Installing of ROS2 Humble](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Installing%20of%20ROS2%20Humble.md)
## Building ROS2 Message Package
The steps of building a package of ROS2 can be found [Here](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

Or follow the below steps:
In the example we will be generating messages from unity of a objects x,y,z position and x,y,z,w rotation data. For that a ROS2 msgs package will be created.
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
7. Open package.xml file to add the code below:
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
8. Then create a folder in the the package folder called `msg`. Open the `msg` folder to create a text file called `UnityCubePosition.txt` later change the extention to `.msg` or `UnityCubePosition.msg`. And add the following lines
   ```
   float64 x
   float64 y
   float64 z
   float64 rotx
   float64 roty
   float64 rotz
   float64 rotw
   ```
9. Go back to ros_ws folder
   ```
   cd ~/ros2_ws
   ```
10. Now to build the package which will also install the package into ros2->install directory. Replaced package name as `matsive_r2msgs`.
   ```
   colcon build --packages-select my_package
   ```
10. Now matsive_r2msgs can be found in ros_ws->install folder.

## Building ROS2 package 
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








_end_
<div align="justify">
</div>
<!-- <div align="center">
  <img src="https://github.com/user-attachments/assets/65232309-1d2b-44ab-8bba-23993dca465d" alt="Screenshot" width="800"/>
</div>
<br />
![Screenshot from 2024-10-07 20-47-17](https://github.com/user-attachments/assets/12e8d452-b3e4-499d-a7ce-59f5c86420c7)
<div align="center">
  <img src="https://github.com/user-attachments/assets/12e8d452-b3e4-499d-a7ce-59f5c86420c7" alt="Screenshot" width="800"/>
  ![Screenshot from 2024-10-07 21-21-22](https://github.com/user-attachments/assets/0806faeb-d7c1-495b-b55a-d9f7d084b547)
  ![image](https://github.com/user-attachments/assets/080a5f05-d9f4-4b8d-bad0-63b8e92c33f2)
</div>-->


# _# END_

## Unity Section<br />
### Unity Hub<br />
Install the Unity Hub from [here](https://docs.unity3d.com/hub/manual/InstallHub.html#install-hub-linux). <br />

or use the same steps below:<br />
To install the _**Unity Hub**_ on a Debian or Ubuntu Linux distribution, you need to add the Unity Hub Debian repository along with the public signing key to verify the integrity of the packages.
1. To add the public signing key, run the following command:
```
wget -qO - https://hub.unity3d.com/linux/keys/public | gpg --dearmor | sudo tee /usr/share/keyrings/Unity_Technologies_ApS.gpg > /dev/null
```
2. To add the Unity Hub repository, you need an entry in /etc/apt/sources.list.d. Run the following command to add the Unity Hub repository:
```
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/Unity_Technologies_ApS.gpg] https://hub.unity3d.com/linux/repos/deb stable main" > /etc/apt/sources.list.d/unityhub.list'
```
3. Update the package cache and install the package:
```
sudo apt update
sudo apt-get install unityhub
```
Note: For some systems, you may need to ensure the following: <br />
 - The directory /usr/share/keyrings exists. <br />
 - The user or group installing the Hub has write permissions to the /usr/share/keyrings directory. <br />
 - The user or group installing Hub has at least read permissions to the resulting file Unity_Technologies_ApS.gpg. <br />
 
To remove the Unity Hub from the system, run the following command:
``
sudo apt-get remove unityhub
``
### Unity version 2022.3.29f1
Go to [Unity Download Archive](https://unity.com/releases/editor/archive) to install the specified version into the Unity Hub.
### Unity Create Project
Create a project in Unity. Name given in this example is "Unity_ROS2_msgs". Selected Unity version is 2022.3.29f1.<br />
<!-- ![Screenshot from 2024-10-07 20-29-14](https://github.com/user-attachments/assets/65232309-1d2b-44ab-8bba-23993dca465d)  -->
<p float="left">
  <img src="https://github.com/user-attachments/assets/65232309-1d2b-44ab-8bba-23993dca465d" width="370" />
  <img src="https://github.com/user-attachments/assets/12e8d452-b3e4-499d-a7ce-59f5c86420c7" width="450" /> 
</p>

### Adding Visual Studio Code to Unity
(null right now)

### Creating Environment and ROS2 Messages
Similar, ROS2 message generation can also be found in [ROS–Unity Integration: Publisher](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/publisher.md) and [ROS–Unity Integration: Subscriber](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/subscriber.md)

In the Hierarchy the project scenes can be found. Scene or environments are the things that will contain different game_objects which will construct the game. The current open scene SampleScene Contrains Main Camera & Directional Light. Click the "+" icon beside Hierarchy or Right Click under the scene will give option to create game_objects.<br />

**Environment:**
 - A Cube Object was created.<br />
 - A Plane was created.<br />
 - A Material Was created and its color was set as Blue.<br />
 - The Planes color was set as the newly created color material by dragging the material upon the plane.<br />
 - Double Clicking the cube will center the cube in the scene. <br />
<p float="left">
 <img src="https://github.com/user-attachments/assets/0806faeb-d7c1-495b-b55a-d9f7d084b547" width="420" />
 <img src="https://github.com/user-attachments/assets/080a5f05-d9f4-4b8d-bad0-63b8e92c33f2" width="390" /> 
</p>

**ROS-TCP-Connector Package Install:** <br />

Install ROS-TCP-Connector Package from [ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector/tree/main).

Or use the same steps below. This [ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector/tree/main) repository contains two Unity packages: the ROS TCP Connector, for sending/receiving messages from ROS, and the Visualizations Package, for adding visualizations of incoming and outgoing messages in the Unity scene.

1. Using Unity 2020.2 or later, open the Package Manager from `Window` -> `Package Manager`.
2. In the Package Manager window, find and click the + button in the upper lefthand corner of the window. Select `Add package from git URL....`
   
    ![image](https://user-images.githubusercontent.com/29758400/110989310-8ea36180-8326-11eb-8318-f67ee200a23d.png)
   
4. Enter the git URL for the desired package. to declare a specific package version, or exclude the tag to get the latest from the package's `main` branch.
    1. For the ROS-TCP-Connector, enter
       ```
       https://github.com/Unity-Technologies/ROS-TCP-Connector.git?path=/com.unity.robotics.ros-tcp-connector
       ```
    2. For Visualizations, enter
       ```
       https://github.com/Unity-Technologies/ROS-TCP-Connector.git?path=/com.unity.robotics.visualizations
       ```
5. Click `Add`.

To install from a local clone of the [ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector/tree/main) repository, see [installing a local package](https://docs.unity3d.com/Manual/upm-ui-local.html) in the Unity manual.

### *NOTE: you can append a version tag to the end of the git url, like `#v0.4.0` or `#v0.5.0`

**ROS2 Message:** <br />
 - After installation of ROS-TCP-Connector Package in unity go to `Robotics`-> `ROS setting`.<br />
 - And change the protocol to ROS2 as given in image.<br />
 
![image](https://github.com/user-attachments/assets/c72c3e62-a426-402b-9fe6-0d2039c71dc5)

 - A C# Script `UnityMessageToTCP.cs` was create and the following code was written in it.
```
(null null)
```
 - Create new empty gameobject and name it `RosPublisher`.
 - Add the created script to the new gameobject **RosPublisher** in the scene by inspection-> add component -> UnityMessageToTCP.cs or dragging it to the empty area below add component in inspection.<br />
(image null null)
 - In that Component add the Cube gameobject by clicking the empty place and selecting the cube or dragging the cube to that empty place.<br />
(image null null)

Unity game can not be played until ROS-message is generated. To do that a ROS2 message package will be created.

