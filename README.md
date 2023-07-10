# Problem

### Description:

In the field of robotics, tracking the position of a device is a common problem. Usually the build in solutions are not as accurate as the developers would like or the synchronization of different sensors are too difficult. One part of the problem is to project the depth data to a predefined plane and to reduce the measurement error of the sensor. Optionally the built in IMU (inertial measurement unit) can be used to track the movement of the device in addition to image processing. The sensor for this project is the Intel RealSense Depth Camera D435i, which we can use with the pyrealsense2 module.

### Roadmap:

- Install neceserry tools
    > Goal: Set up a work environment for the project.
    - IDE (Jupyter, Spyder, PyCharm, VS Code, ...)
    - pyrealsense2
    - cv2
    - numpy


- Check the usage of the Intel Realsense device
    > Goal: Acquire the necessary knowledge to work in the project.
    - BGR image
    - Depth data (and image)
    - IMU data


- Calibration problem
    > Goal: Create a process where the camera calibrates itself after starting.
    - Set up a physical environment to measure and collect data
    - Define and create reference points/objects
    - Define and calculate correction constants (use Euclidean distance)
    - Coding and testing


- Projection problem
    > Goal: Create a projected map on the plane of the floor based on the camera data.


- Tracking problem
    > Goal: Use the BGR and Depth data to follow the movement of the camera in the 3D(or 2D) space.
