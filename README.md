# Camera-turret
A simple ROS-Gazebo package to control the rotation of a two axis camera

## Introduction
The following respository holds a ROS package that simulates a 2DOF camera turret which can be controlled with a joystick.

## How to get started
Just follow the next steps:
1. Install the package
2. Plug in the joystick
3. Execute `roslaunch XXXX.launch`
4. Wait until Gazebo is loaded
5. Press the directional keys
6. The camera should be moving

## How it works
There are three main parts you should care look around:
* script: It holds the code for remapping the joystick's keystrokes into position commands received by the camera-turret.
* urdf: It holds the URDF file that defines the camera-turret's dinamics and kinematics.
* launch file: It holds the code that will be executed by roslaunch and it will set up all the nodes and simulation accordingly.

## Getting into details
This repositotries can be divided into two main components, the simulation and the ROS enviroment. Below code is for more in-depth details and all the below explanation is done automatically by the system when calling by `roslaunch XXXX.launch`.

### ROS enviroment
For controlling the "robot", we want to pass it a couple of positional commands to control the 2DOF of the system. As in this case we will be connecting the ROS enviroment to a simulated world, we add the `libgazebo_ros_control.so` plugin to the URDF to allow a communication between ROS and Gazebo and we add some `transmission_interface`s to allow for a positional control.

Once the urdf is prepared, we create a simple script ("joy_to_command.py") that converts the readings from a joysticks into an actual commands for the "robot". The reading of the joysticks is handled by the "Joy_node" which is loaded from the ["Joy" ROS package](https://wiki.ros.org/joy). All this gives a result the following graph:

!!!! INSERT IMAGE !!!!


### Gazebo simulation






## Requirements
You should install the following:
* ROS-lunar
* Gazebo
* Python
* Joy (ROS package)
* USB joystick
















