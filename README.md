# Integration of CoppeliaSim, Unity, and RViz with ROS2  

## Project Description  
This repository demonstrates the connection and integration of **CoppeliaSim**, **Unity**, and **RViz** using **ROS2** for robotics simulation and visualization. The goal is to enable seamless communication between these tools to simulate a robot’s movement in CoppeliaSim, visualize it in RViz, and render it in Unity for immersive experiences.  

The repository includes configurations, scripts, and documentation to help users set up the system and achieve a synchronized workflow.  

---

## Features  
- **CoppeliaSim**: Simulates robot motion and dynamics.  
- **ROS2**: Manages communication between tools using topics and TF for real-time position and movement data.  
- **RViz**: Visualizes the robot’s 3D model, trajectory, and sensor data.  
- **Unity**: Provides a realistic 3D environment for advanced rendering and immersive interaction.  

---

## Author Information  
- **Name**: Jose Pablo Cobos Austria 
- **Student ID**: A01274631  
- **Institution**: ITESM    

---

## Prerequisites  

### Software Requirements  
- [CoppeliaSim](https://www.coppeliarobotics.com/) (latest version)  
- [Unity3D](https://unity.com/) (2021.3 or later recommended)  
- [ROS2](https://docs.ros.org/en/rolling/Installation.html) (Rolling or Humble version)  
- RViz2 (part of ROS2 installation)  

### Programming Languages  
- Python or C++ (ROS2 node development)  
- C# (Unity scripting)  

### Dependencies  
Install the following ROS2 packages:  
```bash
sudo apt install ros-humble-tf2-tools ros-humble-rviz2 ros-humble-geometry-msgs ros-humble-nav-msgs
