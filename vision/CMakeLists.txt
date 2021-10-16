cmake_minimum_required(VERSION 3.0.2)
project(vision)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  opencv2
  cv_bridge
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(
  PROGRAMS
    nodes/ball_detect
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_python_setup()

