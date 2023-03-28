execute_process(COMMAND "/home/insaf/ros_ws/build/modbus/modbus_cognex_insight/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/insaf/ros_ws/build/modbus/modbus_cognex_insight/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
