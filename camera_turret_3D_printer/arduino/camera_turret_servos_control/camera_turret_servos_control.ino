/*
 * Camera turret 2 servo control for ROS
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;

Servo servo1;
Servo servo2;

float angle;

void servo1_cb( const std_msgs::UInt16& cmd_msg){

  // Check angle
  angle = cmd_msg.data;
  if (angle > 180) {
    angle = 180;
  } 
  else if (angle < 0) {
    angle = 0;
  }  
  
  servo1.write(angle); //set servo1 angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}

void servo2_cb( const std_msgs::UInt16& cmd_msg){

  // Check angle
  angle = cmd_msg.data;
  if (angle > 180) {
    angle = 180;
  } 
  else if (angle < 0) {
    angle = 0;
  }  
  
  servo2.write(angle); //set servo1 angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}

ros::Subscriber<std_msgs::UInt16> sub1("servo1", servo1_cb);
ros::Subscriber<std_msgs::UInt16> sub2("servo2", servo2_cb);

void setup(){
  //pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub1);
  nh.subscribe(sub2);
  
  servo1.attach(6); //attach it to pin 6
  servo2.attach(9); //attach it to pin 9
}

void loop(){
  nh.spinOnce();
  delay(1);
}
