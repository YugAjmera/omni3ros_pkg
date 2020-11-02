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

Model from: [https://github.com/GuiRitter/OpenBase](https://github.com/GuiRitter/OpenBase)

- To view the model with controllers : `roslaunch omni3ros_pkg velocity_controller.launch `

- To view RVIZ model : `roslaunch omni3ros_pkg urdf_rviz_view.launch`

- Control the robot using keyboard keys: [teleop_keyboard_omni3](https://github.com/YugAjmera/teleop_keyboard_omni3)

If our work is helpful to you, please kindly cite our paper as:
```
@inproceedings{mishra2019ego,
  title={Ego-Centric framework for a three-wheel omni-drive Telepresence robot},
  author={Mishra, Ruchik and Ajmera, Yug and Mishra, Nikhil and Javed, Arshad},
  booktitle={2019 IEEE International Conference on Advanced Robotics and its Social Impacts (ARSO)},
  pages={281--286},
  year={2019},
  organization={IEEE}
}
```

![](screenshots/Screenshot%20from%202019-02-27%2000-17-33.png)


