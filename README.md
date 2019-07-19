# Camera-turret
Simple ROS packages to control and simulate the rotation of a two axis camera with a joystick.

<p align="middle">
  <img src="/images/Joystick being played.gif" alt="Joystick being played" width=300>

  <img src="/images/Real controlled camera.gif" alt="Real 3D printed camera controlled by a joystick.gif" width=300>

  <img src="/images/Controlled camera.gif" alt="Simulation of a joystick controlled camera.gif" width=300>
</p>



## 1. Introduction
The following repository holds two ROS packages that simulate and control a 2DOF camera turret which can be controlled with a joystick.

Each package includes:

1. camera_turret: It holds a ROS-Gazebo package to **simulate the control** of the two axis camera with a joystick.
2. camera_turret_3D_printer: It holds a ROS package to **move the 3D printed** two axis camera with a joystick using an Arduino. 

## 2. Real Camera-turret
### 2.1. How to get started
Just follow the next steps:

1. Install the `camera_turret_3D_printer` package
2. [3D print the camera-turret and assemble the pieces](#print)
3. [Setup the electronics](#electronics)
2. Plug in the joystick
3. Plug in the camera
3. Execute `roslaunch launchMe.launch`
4. Wait until everything is ready
5. Press the directional keys on the joystick
6. The camera-turret should be moving!


### <a name="print"></a> 2.2. Print the pieces
For those of you who don't own a 2 axis camera, look at [STL files](https://github.com/DAguirreAg/Camera-turret/tree/master/STL%20files) of this repository. Here I included the STL files I used to create the model you see here, so you can 3D print the same camera-turret I used:

<p align="middle">
  <img src="/images/Camera_turret assembled.png" alt="STL files assembled" width=400>
</p>

### <a name="electronics"></a> 2.3. Setup the electronics
The servomotors' control is done using an Arduino UNO. However, keep in mind that the power output of the Arduino UNO microcontroller is limited, so an external power supply is recommended in order to avoid damaging the microcontroller. Please follow this schematics in order to setup your electronics:

<p align="middle">
  <img src="/images/Electronics assembled.jpg" alt="Electronics" width=400>
</p>

Don't forget to load the program included [here](https://github.com/DAguirreAg/Camera-turret/tree/master/camera_turret_3D_printer/arduino/camera_turret_servos_control) in your Arduino UNO.


### 2.4. How the ROS package is divided
There are three main parts you should care about:

* script: It holds the code for remapping the joystick's keystrokes into position commands received by the Arduino UNO microcontroller.
* Arduino: It holds the Arduino's file to receive and control the servomotors.
* launch file: It holds the code that will be executed by roslaunch and it will set up all the nodes accordingly.

### 2.5. Getting into details
The way this ROS package works is as follows:

1. The `joy_node` reads the pressed axes and buttons and sends them to the `joy_to_command` node
2. `joy_to_command` continuously reads the `joy_node`'s data, updates the angle of each servomotor and sends the angle to the `serial_node`.
3.  `serial_node` continuously reads the commands and positions each servomotors accordingly 


### 2.6. Requirements
You should install/have the following:
* ROS-lunar
* Python
* Joy (ROS package)
* USB joystick
* USB camera
* Arduino UNO
* Two servomotors

## 3. Simulated Camera-turret
### 3.1. How to get started
Just follow the next steps:

1. Install the `camera_turret` package
2. Plug in the joystick
3. Execute `roslaunch launchMe.launch`
4. Wait until Gazebo is loaded
5. Press the directional keys on the joystick
6. The camera-turret should be moving!

### 3.2. How the ROS package is divided
There are three main parts you should care about:
* script: It holds the code for remapping the joystick's keystrokes into position commands received by the camera-turret.
* urdf: It holds the URDF file that defines the camera-turret's dynamics and kinematics.
* launch file: It holds the code that will be executed by roslaunch and it will set up all the nodes and simulation accordingly.

### 3.3. Getting into details
This repository can be divided into two main components, the simulation and the ROS environment. Below code is for a more in-depth explanation, which you shouldn't care about as it is done automatically by the system when using `roslaunch launchMe.launch`.

#### 3.3.1. ROS environment
For controlling the "robot", we want to pass a couple of positional commands to control the 2DOF of the system. As in this case we will be connecting the ROS environment to a simulated world, we add the `libgazebo_ros_control.so` plugin to the URDF to allow a communication between ROS and Gazebo and we add some `transmission_interface`s to allow for a positional control.

Once the urdf is prepared, we create a simple script ("joy_to_command.py") that converts the readings from a joystick into an actual commands for the "robot". The reading of the joysticks is handled by the "Joy_node" which is loaded from the ["Joy" ROS package](https://wiki.ros.org/joy). All this gives a result the following graph:

<p align="center">
  <img src="images/Joystick reader-sender setup.jpg" width=600><br/>
  <i>Joystick reader-sender setup</i>
</p>

#### 3.3.2. Gazebo simulation
The camera-turret is composed of 3 links, the base_link, the mobile_link and the camera_link. There are two joints, one between the base_link and the mobile_link and another one between the mobile_link and the camera_link. Below you can find the described setup:

<p align="middle">
  <img src="/images/Gazebo setup normal view.png" alt="Gazebo setup normal view" >
  <img src="/images/Gazebo setup wireframe view.png" alt="Gazebo setup wireframe view" >
</p>

Once everything is setup, the whole result should be the following:
<p align="center">
  <img src="images/Complete setup.jpg" width=900><br/>
  <i>Complete ROS setup</i>
</p>

### 3.4. Requirements
You should install/have the following:
* ROS-lunar
* Gazebo
* Python
* Joy (ROS package)
* USB joystick

