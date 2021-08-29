execute_process(COMMAND "/home/suryak/ECE3091-S2-2021/build/diff_drive/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/suryak/ECE3091-S2-2021/build/diff_drive/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
