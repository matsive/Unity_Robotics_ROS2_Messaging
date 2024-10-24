# Unity Section
[Go To Main Page
](https://github.com/matsive/Unity_Robotics_ROS2_Messaging?tab=readme-ov-file)
## Part 8. Unity Publish & ROS Subscribe MSGS

**Unity Script for Publishing Messages:** 
 - A C# Script `UnityMessageToTCP.cs` was create and the following code was written in it.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.MatsiveR2msgs;

public class NewBehaviourScript : MonoBehaviour
{
    ROSConnection ros;
    public string topicName = "CubePos";

    // The game object
    public GameObject cube;
    // Publish the cube's position and rotation every N seconds
    public float publishMessageFrequency = 0.5f;

    // Used to determine how much time has elapsed since the last message was published
    private float timeElapsed;

    void Start()
    {
        // start the ROS connection
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<UnityCubePositionMsg>(topicName);
    }

    private void Update()
    {
        timeElapsed += Time.deltaTime;

        if (timeElapsed > publishMessageFrequency)
        {
            cube.transform.rotation = Random.rotation;

            UnityCubePositionMsg cubePos = new UnityCubePositionMsg(
                new double[] { (double)cube.transform.position.x },
                new double[] { (double)cube.transform.position.y },
                new double[] { (double)cube.transform.position.z },
                new double[] { (double)cube.transform.rotation.x },
                new double[] { (double)cube.transform.rotation.y },
                new double[] { (double)cube.transform.rotation.z }

            );

            // Finally send the message to server_endpoint.py running in ROS
            ros.Publish(topicName, cubePos);

            timeElapsed = 0;
        }
    }
}
```
 - Create new empty gameobject and name it `RosPublisher`.
 - Add the created script to the new gameobject **RosPublisher** in the scene by inspection-> add component -> UnityMessageToTCP.cs or dragging it to the empty area below add component in inspection.<br />
 - In that Component add the Cube gameobject by clicking the empty place and selecting the cube or dragging the cube to that empty place.<br />
 - After doing this running the Unity Game will make the cube rotate and also show error message in the terminal as ROS2 is not connected to Unity yet.

<!-- ![image](https://github.com/user-attachments/assets/9cb4d73e-218e-4f22-8706-817278693ebe)  -->
<p float="left">
  <img src="https://github.com/user-attachments/assets/9cb4d73e-218e-4f22-8706-817278693ebe" width="600" />
</p>

To make the connection between Unity and ROS2. The ROS2 package for subscribing to the unity messages need to run 1st. Then running the play button in unity will establish the connection. like below in terminal.


`INFO] [1729734446.178315156] [UnityEndpoint]: Starting server on 0.0.0.0:10000` <br />
`[INFO] [1729734446.523227541] [UnityEndpoint]: Connection from 127.0.0.1` <br />
`[INFO] [1729734446.549483530] [UnityEndpoint]: RegisterSubscriber(/tf, <class 'tf2_msgs.msg._tf_message.TFMessage'>) OK` <br />
`[INFO] [1729734446.554115496] [UnityEndpoint]: RegisterPublisher(/CubePos, <class 'matsive_r2msgs.msg._unity_cube_position.UnityCubePosition'>) OK `<br />

<!-- ![image](https://github.com/user-attachments/assets/73507b37-4efd-4c8f-bc99-721f44133598)-->
<p float="left">
  <img src="https://github.com/user-attachments/assets/73507b37-4efd-4c8f-bc99-721f44133598" width="600" />
</p>

