# Unity_Robotics_ROS2
### Follow the main branch of this repository only
This repository demonstrates how to set up Unity-Robotics-Hub to send messages to a TCP server and subscribe to those messages using ROS2. <br />
(overall image)
## Software
- [Unity Hub](https://docs.unity3d.com/hub/manual/InstallHub.html#install-hub-linux)
- [Unity version 2022.3.29f1](https://unity.com/releases/editor/archive)
- ROS2 Humble
## Unity Section
### _Unity Hub_
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
### _Unity version 2022.3.29f1_
Go to [Unity Download Archive](https://unity.com/releases/editor/archive) to install the specified version into the Unity Hub.
### _Unity Project_
<!-- ![Screenshot from 2024-10-07 20-29-14](https://github.com/user-attachments/assets/65232309-1d2b-44ab-8bba-23993dca465d)  -->
<div align="center">
  <img src="https://github.com/user-attachments/assets/65232309-1d2b-44ab-8bba-23993dca465d" alt="Screenshot" width="500"/>
</div>




## ROS2 Section
