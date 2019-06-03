#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

pub = rospy.Publisher("keys_pressed", String, queue_size=10)

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def keyboard_reader():

    rospy.init_node("keyboard_reader", anonymous=False)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        getch = _Getch()
        keyPressed = getch.__call__()

        #Send the message
        pub.publish(keyPressed)
        rate.sleep()

if __name__ == "__main__":
    keyboard_reader()

