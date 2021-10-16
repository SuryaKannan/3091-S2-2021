cmake_minimum_required(VERSION 3.0.2)
project(control)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(
  PROGRAMS
    nodes/controller
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_python_setup()

