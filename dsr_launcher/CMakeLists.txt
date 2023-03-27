cmake_minimum_required(VERSION 3.0.2)
project(dsr_launcher)

find_package(catkin REQUIRED COMPONENTS roslaunch)

catkin_package()

#############
## Install ##
#############

## Mark other files for installation (e.g. launch and bag files, etc.)
install(
	DIRECTORY launch rviz worlds
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  find_package(catkin REQUIRED COMPONENTS rostest)
  add_rostest(test/single_robot_gazebo.test)
  add_rostest(test/single_robot_rviz_gazebo.test)
  add_rostest(test/single_robot_rviz.test)
endif()