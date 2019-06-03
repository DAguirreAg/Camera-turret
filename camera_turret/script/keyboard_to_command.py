#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float64

global position1, position2
position1 = 0.0
position2 = 0.0

pub1 = rospy.Publisher("command1", Float64, queue_size=10) #Right wheel steering
pub2 = rospy.Publisher("command2", Float64, queue_size=10) #Left wheel turning

def callback(data):
    keyPressed = data.data
    global position1, position2
    
    # Keys: Up: 8, down: 2, left: 4, Right: 6, Reset: 0
    if (keyPressed == "4"):
        position1 = position1 + 1.0*3.14159/180.0
        
    elif (keyPressed == "6"): 
        position1 = position1 - 1.0*3.14159/180.0        
        
    elif (keyPressed == "0"):
        position1 = 0.0
        position2 = 0.0
    
    elif (keyPressed == "8"):
        position2 = position2 + 1.0*3.14159/180.0

    elif (keyPressed == "2"):
        position2 = position2 - 1.0*3.14159/180.0  
  

    #Prepare and send messages
    if (keyPressed =="4" or keyPressed =="6"):
        pub1.publish(position1)

    if (keyPressed =="8" or keyPressed =="2"):           
        pub2.publish(position2)
    
    if (keyPressed =="0"):
        pub1.publish(position1)
        pub2.publish(position2)

def keyboard_to_command():

    print("Keys: Up: 8 \n      Down: 2 \n      Left: 4 \n      Right: 6 \n      Reset: 0")

    rospy.init_node("keyboard_to_command", anonymous=False)
    sub = rospy.Subscriber("keys_pressed", String, callback)     
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    keyboard_to_command()

