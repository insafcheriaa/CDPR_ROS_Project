# CDPR_ROS_Project

#ROS Workspace
This is a ROS workspace that contains a package called "my_package" which itself contains two nodes, "teleop_node.py" and "modbus.py", 
that are used to control a URDF model of a robot and communicate with a PLC via Modbus protocol, respectively.

#Prerequisites
To run this workspace, you need to have the following installed:

ROS
Python
Modbus library for Python (pymodbus)

#Installation
To use this workspace, follow these steps:

*Clone this repository.
**Navigate to the src directory.
***Run catkin_init_workspace to initialize the workspace.
****Run cd .. to navigate to the root of the workspace.
*****Run catkin_make to build the workspace.
******Source the workspace using source devel/setup.bash.

#Usage
To use the nodes in this workspace, follow these steps:

*Launch all nodes using the test.launch file located in the launch directory by typing this command:
roslaunch my_package test.launch

**The following command allows you to use the teleop_node.py script to control the URDF model of the robot visualized on RViz:
rosrun my_package teleop_node.py

***In another terminal, use the modbus.py script to communicate with the PLC running the following:
rosrun my_package modbus.py

#Contributing
If you would like to contribute to this project, please follow these guidelines:

*Fork this repository.
**Create a new branch for your changes.
***Make your changes and commit them.
****Push your changes to your fork.
*****Create a pull request to merge your changes back into the main repository.

#Credits
The code in this repository was written by Insaf Cheriaa.

#License
This project is licensed under the MIT license. 
Please review the terms of the license carefully and consult with your internship advisor or legal counsel to ensure that it meets the specific needs of your project.
