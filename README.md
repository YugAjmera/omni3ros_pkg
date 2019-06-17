# omni3ros_pkg

## A ROS Package for three-wheeled omnidirectional robots

### Getting Started

- `cd catkin_ws/src`
-  Clone this repo here : `git clone "https://github.com/YugAjmera/omni3ros_pkg"`
- `cd ..` (Go back to catkin_ws/)
- `catkin_make`
- `source ./devel/setup.bash`
- `source ~/.bashrc`

### Run

- To view the model in Gazebo : ` roslaunch omni3ros_pkg urdf_gazebo_view.launch `

- To view the model with controllers : `roslaunch omni3ros_pkg velocity_controller.launch `

- To view RVIZ model : `roslaunch omni3ros_pkg urdf_rviz_view.launch`

![](screenshots/Screenshot%20from%202019-02-27%2000-17-33.png)

- Control the robot using keyboard keys: [teleop_keyboard_omni3](https://github.com/YugAjmera/teleop_keyboard_omni3)
