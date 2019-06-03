#!/usr/bin/env python

import rospy
import random
import time
from sensor_msgs.msg import Joy
from std_msgs.msg import String, Float64

pub1 = rospy.Publisher('command1', Float64, queue_size=10) #Left wheel steering
pub2 = rospy.Publisher('command2', Float64, queue_size=10) #Right wheel steering

#General variables
position1 = 0.0
position2 = 0.0

mag1 = 0.0
mag2 = 0.0

def callback(data): 

    #Extract data
    axes = data.axes 
    buttons = data.buttons 
    
    #Joystick buttons: 1 2 3 4
    b1 = buttons[0]
    b2 = buttons[1]
    b3 = buttons[2]
    b4 = buttons[3]
    startkey = buttons[9]
    
    #Joystick keys: left/right up/down 
    lr = axes[6] # Left:1.0   Right:-1.0
    ud = axes[7] # Up:1.0     Down: -1.0
    
    global position1, position2, mag1, mag2

    # Change values when the pressed keys change the sign
    mag1 = lr
    mag2 = ud

    if (startkey == 1.0): 
        mag1 = 0.0
        mag2 = 0.0
        position1 = 0.0
        position2 = 0.0
        
    
def updateValues():
    global position1, position2, mag1, mag2
    position1 = position1 + mag1*(5.0*3.15149/180.0)   
    position2 = position2 + mag2*(5.0*3.15149/180.0)
      
    
def joy_to_command():

    rospy.init_node('joy_to_command', anonymous=False)
    sub = rospy.Subscriber("joy", Joy, callback)    
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # Update values
        updateValues()
        
        # Publish values    
        pub1.publish(position1)
        pub2.publish(position2)
        rate.sleep()

if __name__ == '__main__':
    joy_to_command()
