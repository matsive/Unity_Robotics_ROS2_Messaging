# Unity_Robotics_ROS2
### Follow the main branch of this repository only
This repository demonstrates how to set up Unity-Robotics-Hub to send messages to a TCP server and subscribe to those messages using created ROS2 package. Summarization of all data. <br />
(overall image)
# Software
- [Unity Hub](https://docs.unity3d.com/hub/manual/InstallHub.html#install-hub-linux)
- [Unity version 2022.3.29f1](https://unity.com/releases/editor/archive)
- [ROS2 Humble for Ubuntu](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)
# ROS2 Section (mabye add this 1st)
## Installing of ROS2 Humble
Installation process and files can be found at [Ubuntu (deb packages) ROS2 Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)

Or follow the same steps below:<br />

Set locale:<br />
Make sure you have a locale which supports UTF-8. If you are in a minimal environment (such as a docker container), the locale may be something minimal like POSIX. We test with the following settings. However, it should be fine if you’re using a different UTF-8 supported locale.<br />
(Triple Click on a line to select the whole line) <br />

```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

Setup Sources:<br />
You will need to add the ROS 2 apt repository to your system.<br />
First ensure that the Ubuntu Universe repository is enabled.<br />
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```
Now add the ROS 2 GPG key with apt.
```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Then add the repository to your sources list.
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
Install ROS 2 packages:
Update your apt repository caches after setting up the repositories.
```
sudo apt update
```
ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.
```
sudo apt upgrade
```
`
Warning ::::
Due to early updates in Ubuntu 22.04 it is important that systemd and udev-related packages are updated before installing ROS 2. The installation of ROS 2’s dependencies on a freshly installed system without upgrading can trigger the removal of critical system packages.
Please refer to ros2/ros2#1272 and Launchpad #1974196 for more information.
` 
<br />
Desktop Install (Recommended): ROS, RViz, demos, tutorials.
```
sudo apt install ros-humble-desktop
```

**Environment setup**
Sourcing the setup script:
Set up your environment by sourcing the following file.
```
# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/humble/setup.bash
```
### *NOTE: The ROS2 will not run unless the setup.bash is sourced each time the device (pc) restarts.

Try some examples
Talker-listener
If you installed ros-humble-desktop above you can try some examples.
In one terminal, source the setup file and then run a C++ talker:
```
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```
In another terminal source the setup file and then run a Python listener:
```
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
```
You should see the talker saying that it’s Publishing messages and the listener saying I heard those messages. This verifies both the C++ and Python APIs are working properly. Hooray!

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
11. Now matsive_r2msgs can be found in ros_ws->install folder.

## Building ROS2 package 
    










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

