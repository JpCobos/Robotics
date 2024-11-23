# Reto - Proyecto de Robótica
#
## Descripción del Proyecto
Esta carpeta contiene los archivos relacionados con el **Reto** en el contexto de simulación y visualización robótica. Este proyecto utiliza herramientas como **CoppeliaSim**, **ROS2** y **RViz**, integradas para explorar, simular y analizar el movimiento de robots en un entorno virtual.

Incluye la escena de un **Puzzlebot** para CoppeliaSim, junto con un workspace ROS2 preconfigurado con los nodos y paquetes necesarios para la integración con Unity y RViz.

---

## Estructura de la Carpeta
```plaintext
Reto/
│
├── CoppeliaSim/
│   ├── Puzzlebot_scene.ttt     # Escena de CoppeliaSim con el modelo Puzzlebot.
│   └── coppelia_publisher.lua  # Script LUA para publicar datos desde CoppeliaSim.
│
├── Movement/
│   ├── src/                    # Aquí estan todos los paquetes de ROS2 utilizados
│   ├── build/                  # Archivos temporales de compilación.
│   ├── install/             p   # Paquetes compilados y listos.
│   ├── Log/                    # Registros de compilación y ejecución.
│   └── README.md               # Detalles del workspace.
│
└── README.md                   # Este archivo.
