# Integración de CoppeliaSim, Unity y RViz con ROS2  

## Descripción del Proyecto  
Este repositorio demuestra la conexión e integración de **CoppeliaSim**, **Unity** y **RViz** utilizando **ROS2** para la simulación y visualización de robots. El objetivo es habilitar una comunicación fluida entre estas herramientas para simular el movimiento de un robot en CoppeliaSim, visualizarlo en RViz y renderizarlo en Unity para experiencias inmersivas.  

El repositorio incluye configuraciones, scripts y documentación para ayudar a los usuarios a configurar el sistema y lograr un flujo de trabajo sincronizado.  

---

## Características  
- **CoppeliaSim**: Simula el movimiento y las dinámicas del robot.  
- **ROS2**: Gestiona la comunicación entre herramientas usando tópicos y TF para datos en tiempo real de posición y movimiento.  
- **RViz**: Visualiza el modelo 3D del robot, su trayectoria y los datos de sensores.  
- **Unity**: Proporciona un entorno 3D realista para renderización avanzada e interacción inmersiva.  

---

## Información del Autor  
- **Nombre**: Jose Pablo Cobos Austria  
- **Matrícula**: A01274631  
- **Institución**: ITESM  

---

## Requisitos Previos  

### Requisitos de Software  
- [CoppeliaSim](https://www.coppeliarobotics.com/) (última versión)  
- [Unity3D](https://unity.com/) (recomendado 2021.3 o posterior)  
- [ROS2](https://docs.ros.org/en/rolling/Installation.html) (versión Rolling o Humble)  
- RViz2 (incluido con ROS2)  

### Lenguajes de Programación  
- Python o C++ (desarrollo de nodos ROS2)  
- C# (scripting en Unity)  

### Dependencias  
Instala los siguientes paquetes de ROS2:  
```bash
sudo apt install ros-humble-tf2-tools ros-humble-rviz2 ros-humble-geometry-msgs ros-humble-nav-msgs
