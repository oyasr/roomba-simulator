# Roomba Simulator
[iRobot](https://www.irobot.com/) is a company (started by MIT alumni and faculty) that sells the [Roomba vacuuming robot](https://www.irobot.com/). Roomba robots move around the floor, cleaning the area they pass over.

This project simulates the movement of different robotic agents and compares how much time a group of Roomba-like robots will take to clean the floor of a room using different strategies.

As a part of the Artificial Intelligence course, it serves as the semester project.

## Simulation Overview
The following simplified model of a single robot moving in a square 5x5 room should give you some intuition about the system we are simulating.

The robot starts out at some random position in the room, and with a random direction of motion. The illustrations below show the robot's position (indicated by a black dot) as well as its direction (indicated by the direction of the red arrowhead).
| ![alt text](https://courses.edx.org/assets/courseware/v1/a9599c894201ed96d8cd6d1afd778a62/asset-v1:MITx+6.00.2x+3T2020+type@asset+block/files_ps07_files_screen1.png "t0")        | ![alt text](https://courses.edx.org/assets/courseware/v1/178f80c0f5724973720aba89faa741a3/asset-v1:MITx+6.00.2x+3T2020+type@asset+block/files_ps07_files_screen2.png "t1")        | ![alt_text](https://courses.edx.org/assets/courseware/v1/debc0f78a5d1191088c6972e39a4b265/asset-v1:MITx+6.00.2x+3T2020+type@asset+block/files_ps07_files_screen3.png "t2") |
| :-------------: |:-------------:| :-----:|
| ![alt_text](https://courses.edx.org/assets/courseware/v1/300d6494c0f7f83c84efafbc44484973/asset-v1:MITx+6.00.2x+3T2020+type@asset+block/files_ps07_files_screen4.png "t3")       | ![alt_text](https://courses.edx.org/assets/courseware/v1/1a51168c1262621d2a46fbd59f26845b/asset-v1:MITx+6.00.2x+3T2020+type@asset+block/files_ps07_files_screen5.png "t4")       |  |
### Time t = 0
The robot starts at a position in the room with an angle (measured clockwise from "north"). The tile that it is on is now clean.
### Time t = 1
The robot has moved 1 unit in the direction it was facing, cleaning another tile.
### Time t = 2
The robot has moved 1 unit in the same direction, cleaning another tile.
### Time t = 3
The robot could not have moved another unit in the same direction without hitting the wall, so instead it turns to a new random direction.
### Time t = 4
The robot moves along its new direction to cleaning another tile.

## Simulation Details
### Multiple Robots
In general, there are N > 0 robots in the room, where N is given. For simplicity, assume that robots are points and can pass through each other or occupy the same point without interfering.

### Room
The room is rectangular with some integer width w and height h, which are given. Initially the entire floor is dirty. A robot cannot pass through the walls of the room. A robot may not move to a point outside the room.

### Tiles
Robots need to keep track of which parts of the floor have been cleaned. The area of the room is divided into 1x1 tiles (there will be w * h such tiles). When a robot's location is anywhere in a tile, we will consider the entire tile to be cleaned (as in the pictures above). By convention, we will refer to the tiles using ordered pairs of integers: (0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), ..., (w-1, h-1).

### Robot Motion Rules
* Each robot has a position inside the room. We'll represent the position using coordinates (x, y) which are floats satisfying 0 ≤ x < w and 0 ≤ y < h. In our program we'll use instances of the Position class to store these coordinates.
* A robot has a direction of motion. We'll represent the direction using an integer d satisfying 0 ≤ d < 360, which gives an angle in degrees.
* All robots move at the same speed s, a float, which is given and is constant throughout the simulation. Every time-step, a robot moves in its direction of motion by s units.
* If a robot detects that it will hit the wall within the time-step, that time step is instead spent picking a new direction at random. The robot will attempt to move in that direction on the next time step, until it reaches another wall.

### Termination
The simulation ends when a specified fraction of the tiles in the room have been cleaned.

## Project Structure
```
├── roomba-simulator/
    ├── app.py
    ├── visualize.py
    ├── verify_movement35.pyc
    ├── verify_movement36.pyc
    ├── verify_movement37.pyc
    ├── verify_movement38.pyc
```
This is structure has six files:
* *app.py* contains the main program.
* *visualize.py* visualizes the robot's movement.
* *verify_movement35.pyc* is a precompiled module for Python 3.5 that assists with the visualization code.
* *verify_movement36.pyc* is a precompiled module for Python 3.6 that assists with the visualization code.
* *verify_movement37.pyc* is a precompiled module for Python 3.7 that assists with the visualization code.
* *verify_movement38.pyc* is a precompiled module for Python 3.8 that assists with the visualization code.
