#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from pymodbus.client.sync import ModbusTcpClient

def plc_callback(msg, client):
    # Write data to PLC
    client.write_registers(4197, [msg.data])

def main():
    # Initialize ROS node
    rospy.init_node('modbus_node')
    rospy.loginfo("ModBus node has started!")
    
    # Connect to Modbus TCP server
    client = ModbusTcpClient('192.168.1.5', 502)
    client.connect()
    if not client.connect():
        rospy.logerr('Modbus connection failed')
        return
    
    # Create a publisher for each motor
    pub1 = rospy.Publisher('motor1_pos', Int32, queue_size=10)
    pub2 = rospy.Publisher('motor2_pos', Int32, queue_size=10)
    pub3 = rospy.Publisher('motor3_pos', Int32, queue_size=10)
    pub4 = rospy.Publisher('motor4_pos', Int32, queue_size=10)

    rate = rospy.Rate(10) 
    
    while not rospy.is_shutdown():
        # Read the current position of each motor from the PLC
        motor1_pos=client.read_holding_registers(4197, 1).registers[0]
        motor2_pos = client.read_holding_registers(4199, 1).registers[0]
        motor3_pos = client.read_holding_registers(4201, 1).registers[0]
        motor4_pos = client.read_holding_registers(4203, 1).registers[0]

        # Publish the position of each motor
        pub1.publish(motor1_pos)
        pub2.publish(motor2_pos)
        pub3.publish(motor3_pos)
        pub4.publish(motor4_pos)

        # Sleep for the remainder of the loop
        rate.sleep()

    # Disconnect from Modbus TCP server
    client.close()

if __name__ == '__main__':
    main()

    # Subscribe to ROS topic and write data to PLC
    #sub = rospy.Subscriber('plc_control', Int32, plc_callback, client)
    # Spin ROS node
    #rospy.spin()