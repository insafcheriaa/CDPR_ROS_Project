#!/usr/bin/env python3
import rospy #module: provides the basic functionality for creating a ROS node,publishing and subscribing to topics, and handling messages.
from sensor_msgs.msg import JointState #message type used to subscribe to the robot's pulley position.
import sys, select, termios, tty #python modules used for reading keyboard input from the user.
import random
 #=========================================================================================================================
if __name__ == '__main__':
    
    global settings, js_msg
    js_msg=JointState() 
    settings=termios.tcgetattr(sys.stdin) #variable that stores the terminal settings so they can be restored later.
 #=========================================================================================================================
    rospy.init_node("Teleop_node")
    rospy.loginfo("Teleop_node has been stared!") #prints a message to the console.
 #=========================================================================================================================  
    def get_key(): #function which reads a single character from the keyboard input buffer.
    # Change the terminal settings to raw mode
       tty.setraw(sys.stdin.fileno())
    # Wait for input for 0.1 seconds
       select.select([sys.stdin], [], [], 1.0)
    # Read a single character from the input buffer
       key = sys.stdin.read(1)
    # Restore the terminal settings to their original state
       termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
       return key

    def modify_joint_state():
       pulley=['n','n','n','n']
       js_msg.name = ['Pulley1_Joint','Pulley2_Joint','Pulley3_Joint','Pulley4_Joint']
       js_msg.position = [0.0, 0.0, 0.0, 0.0]
       pos = 0.0
       js_msg.header.stamp = rospy.Time.now()
       for i in range(4):
          pulley[i] = input("Change pulley "+str(i+1)+"'s position? [y/n] : ")
          if pulley[i] == 'y':
            try:
                pos = float(input("Enter pulley"+str(i+1)+"'s new position : "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            else:
                js_msg.position[i] = pos
          elif pulley[i] == 'n':
            js_msg.position[i] = 0.0
       pub.publish(js_msg)

    def random_rotation():
       js_msg.name = ['Pulley1_Joint','Pulley2_Joint','Pulley3_Joint','Pulley4_Joint']
       js_msg.header.stamp = rospy.Time.now()
       js_msg.position = [0.0, 0.0, 0.0, 0.0]
       for i in range(4):
      # randomly modify an element in the position array
          if random.random() < 0.5:
             js_msg.position[i] = random.uniform(-2.0,2.0)
       pub.publish(js_msg)
    
    def center_all():
       js_msg.name = ['Pulley1_Joint','Pulley2_Joint','Pulley3_Joint','Pulley4_Joint']
       js_msg.position = [0.0, 0.0, 0.0, 0.0]
       js_msg.header.stamp = rospy.Time.now()
       for i in range(4):
          js_msg.position[i]=0.0
       pub.publish(js_msg)
 #=========================================================================================================================
    pub = rospy.Publisher("joint_states", JointState, queue_size=10)
    rate = rospy.Rate(10)
 #=========================================================================================================================
    while not rospy.is_shutdown():
      print("""\n-------------------CONTROL GUIDE-------------------
            'z'  [Set Positions]
            's'  [Random Rotation]
            'd'  [Center All]
            'q'  [Quit] """)

      key=get_key()
      if key=='z':
          print('\nRotating...')
          modify_joint_state()
      elif key=='s':
          print('\nRandomizing...')
          random_rotation()
      elif key==' ': 
          continue
      elif key=='d':
          print('\nCenterizing...')
          center_all()
      elif key=='q':
          print('\nQuitting...')
          break
      
    rate.sleep() 

