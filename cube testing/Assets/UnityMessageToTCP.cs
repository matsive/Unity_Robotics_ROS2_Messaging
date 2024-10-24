using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.MatsiveR2msgs;

public class UnityMessageToTCP : MonoBehaviour
{
    ROSConnection ros_m;
    string topicName = "/CubePos";

    // The game object
    public GameObject cube;
    // Publish the cube's position and rotation every N seconds
    public float publishMessageFrequency = 0.5f;

    // Used to determine how much time has elapsed since the last message was published
    private float timeElapsed;

    void Start()
    {
        // start the ROS connection
        ros_m = ROSConnection.GetOrCreateInstance();
        ros_m.RegisterPublisher<UnityCubePositionMsg>(topicName);
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
            ros_m.Publish(topicName, cubePos);

            timeElapsed = 0;
        }
    }
}
