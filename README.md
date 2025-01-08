# UAV
## Drone Design and Aerial Robotics


### ROS - Robot development platform
- motors, sensors, software, and batteries all should work together to perform a task. Connect them using ROS tools called topics and messages.
- There is a ROS package for everything: remote control, control trajectory, etc.
- UAV - Unmanned Aerial Vehicle - can be remotely controlled, or the path can be autonomously planned.
- Multirotors - propellers, motors, ESC'c, flight controller, transmitter and receiver, batteries.
- The flight controller (a.k.a FC) is the brain of the aircraft. (Pixhawk) It's a circuit board with sensors that detect the drone's movement and user commands. PID control loop in FC - backbone - proportional, integral, derivative
- Firmware - software program etched in a hardware device - ArduPilot, px4
- before directly controlling a drone - set up a virtual drone and run simulations there
- SITL - Virtual flight controller attached to a 3D model, Gazebo simulation - what is happening to the drone.
- ROS has a subdivision called MAVROS, which converts all commands in our program into messages(Mavlink messages) that can be interpreted by the FC (Flight Controller) to perform a task. When running the code, these messages are transmitted to SITL as we can define which port the messages must be communicated (Each computer has its own port ID).

In simulation:
Program -> Mavros -> Mavlink Messages -> SITL -> Drone in simulation environment.

In real drone:
Program -> Mavros -> Mavlink Messages -> Pixhawk -> Drone movements.

SITL stands for "Software-In-The-Loop." It is a type of simulation used in robotics and unmanned aerial vehicles (UAVs), where the software controlling the vehicle is tested in a simulated environment rather than on a physical vehicle.


### The Drone Dojo
- DRONE DESIGN: THRUST TO WEIGHT RATIO
  WEIGHT is the downward force. Our drone must overcome this force in weight in the opposite direction to fly. 
  F=m, F=(g) —> gravity is constant everywhere.
  THRUST the mass a motor/prop can lift in the air.
  MUST HAVE MORE THRUST THAN WEIGHT TO FLY
  COMMON TWO RATIOS-
    - 4:1 / 11:1 - racing drones
    - normally 2:1 (good), 1.5:1 —> but here less space for payload
- DRONE ANATOMY: GPS/OPTICAL FLOW(with height sensor)
  Basic required sensors for flight-
    - accelerometer
    - gyroscope
  GPS - drone knows where it is in 3D space. It is used in conjunction with a magnetometer - to determine YAW orientation. (NEED TO BE OUTSIDE TO ACCESS SATELLITES.)
  OPTICAL FLOW SENSOR - does not know where it is in 3D space + expensive. It is used in conjunction with height-determining sensors - sonar can fly indoor   
- AUTOPILOTS
  Micro-controller FC- Pixhawk 
    - designed for real-time applications
    - dedicated computing power for flight control firmware, faster computational speed
  Linux FC
    - easy to set and interact with
    - can update the drone firmware wirelessly (if by wifi)
    - not real-time and not seen much in industrial applications
