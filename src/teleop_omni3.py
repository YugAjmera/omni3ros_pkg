#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import sys, select, termios, tty
import rospy

msg = """
Reading from the keyboard  
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 1 unit

anything else : stop

CTRL-C to quit
"""

moveBindings = {
        'i':(1,0,0),
        'o':(1,-1,0),
        'j':(1,1,1),
        'l':(-1,-1,-1),
        'u':(-1,0,1),
        ',':(-1,0,0),
        '.':(1,0,-1),
        'm':(-1,1,0),  
    }

speedBindings={
        'q':(1),
        'z':(-1),
    }

def getKey():
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":

    	settings = termios.tcgetattr(sys.stdin)

	rospy.init_node('vel_Publisher')
	pub = rospy.Publisher('/open_base/back_joint_velocity_controller/command', Float64, queue_size=1)
	pub1 = rospy.Publisher('/open_base/left_joint_velocity_controller/command', Float64, queue_size=1)
	pub2 = rospy.Publisher('/open_base/right_joint_velocity_controller/command', Float64, queue_size=1)

	x = 0
    	y = 0
   	z = 0
	speed = 1.0
	print(msg)
	
	while(1):  
		key = getKey()       
		if key in moveBindings.keys():
                	x = moveBindings[key][0]
                	y = moveBindings[key][1]
                	z = moveBindings[key][2]

		elif key in speedBindings.keys():
                	speed += speedBindings[key][0]
			print(speed)

		else:
                	x = 0
    			y = 0
   			z = 0
                	if (key == '\x03'):
                    		break  
		vel = Float64()
		vel1 = Float64()
		vel2 = Float64()
	
		vel = x
		vel1 = y
		vel2 = z

		pub.publish(vel)
		pub1.publish(vel1)
		pub2.publish(vel2)


