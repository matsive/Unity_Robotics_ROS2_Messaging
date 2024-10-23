# Unity Section
[Go To Main Page
](https://github.com/matsive/Unity_Robotics_ROS2/blob/main/Documentation/ROS2%20Section/Part%201.%20Installing%20of%20ROS2%20Humble.md)
## Part 7. Unity ROS2 Messages Generation
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

**ROS2 Message Generate From Package**

**Unity Script for Publishing Messages:** 
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

