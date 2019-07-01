# Camera-turret
A simple ROS-Gazebo package to control the rotation of a two axis camera with a joystick

<p align="middle">
  <img src="/images/Joystick being played.gif" alt="Joystick being played" width=300>
  <img src="/images/Controlled camera.gif" alt="Camera controlled by a joystick.gif" width=300>
</p>

## Introduction
The following repository holds a ROS package that simulates a 2DOF camera turret which can be controlled with a joystick.

## How to get started
Just follow the next steps:
1. Install the package
2. Plug in the joystick
3. Execute `roslaunch setMeUp.launch`
4. Wait until Gazebo is loaded
5. Press the directional keys
6. The camera should be moving

## How it works
There are three main parts you should care look around:
* script: It holds the code for remapping the joystick's keystrokes into position commands received by the camera-turret.
* urdf: It holds the URDF file that defines the camera-turret's dynamics and kinematics.
* launch file: It holds the code that will be executed by roslaunch and it will set up all the nodes and simulation accordingly.

## Getting into details
This repositories can be divided into two main components, the simulation and the ROS environment. Below code is for more in-depth details and all the below explanation is done automatically by the system when calling by `roslaunch setMeUp.launch`.

### ROS environment
For controlling the "robot", we want to pass it a couple of positional commands to control the 2DOF of the system. As in this case we will be connecting the ROS environment to a simulated world, we add the `libgazebo_ros_control.so` plugin to the URDF to allow a communication between ROS and Gazebo and we add some `transmission_interface`s to allow for a positional control.

Once the urdf is prepared, we create a simple script ("joy_to_command.py") that converts the readings from a joystick into an actual commands for the "robot". The reading of the joysticks is handled by the "Joy_node" which is loaded from the ["Joy" ROS package](https://wiki.ros.org/joy). All this gives a result the following graph:

<p align="center">
  <img src="images/Joystick reader-sender setup.jpg" width=600><br/>
  <i>Joystick reader-sender setup</i>
</p>

### Gazebo simulation
The camera-turret is composed of 3 links, the base_link, the mobile_link and the camera_link. There are two joints, one between the base_link and the mobile_link and another one between the mobile_link and the camera_link. Below you can find the described setup:

<p align="middle">
  <img src="/images/Gazebo setup normal view.png" alt="Gazebo setup normal view" >
  <img src="/images/Gazebo setup wireframe view.png" alt="Gazebo setup wireframe view" >
</p>

Once everything is setup, the whole result should be the following:
<p align="center">
  <img src="images/Complete setup.jpg" width=900><br/>
  <i>Joystick reader-sender setup</i>
</p>

## Requirements
You should install the following:
* ROS-lunar
* Gazebo
* Python
* Joy (ROS package)
* USB joystick

