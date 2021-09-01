cmake_minimum_required(VERSION 3.0.2)
project(comms)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(
  PROGRAMS
    nodes/republisher
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_python_setup()

