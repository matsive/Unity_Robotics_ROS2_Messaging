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
# ROS2 Section 
## [Part 1. Install ROS2 Humble](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Part%201.%20Install%20ROS2%20Humble.md)
## [Part 2. Building ROS2 Message Package (Publisher)](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Part%202.%20Building%20ROS2%20Message%20Package.md)
## [Part 3. Building ROS2 package (Subscriber)](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Part%203.%20Building%20ROS2%20package.md)
# Unity Section<br />
## [Part 4. Install Unity Hub](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/Unity%20Section/Part%204.%20Install%20Unity%20Hub.md)<br />
## [Part 5. Install Unity version 2022.3.29f1](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/Unity%20Section/Part%205.%20Install%20Unity%20System.md)
## [Part 6. Unity Create Project & Add Visual Studio Code](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/Unity%20Section/Part%206.%20Unity%20Create%20Project%20%26%20Add%20Visual%20Studio%20Code.md)
## [Part 7. Unity ROS2 Messages Generation](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/Unity%20Section/Part%207.%20Unity%20ROS2%20Messages%20Generation.md)




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




Similar, ROS2 message generation can also be found in [ROS–Unity Integration: Publisher](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/publisher.md) and [ROS–Unity Integration: Subscriber](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/subscriber.md)


### ROS2 Messages
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

