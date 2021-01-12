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
Robots need to keep track of which parts of the floor have been cleaned. The area of the room is divided into 1x1 tiles (there will be w * h such tiles). When a robot's location is anywhere in a tile, we will consider the entire tile to be cleaned. This might not make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation. By convention, we will refer to the tiles using ordered pairs of integers: (0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), ..., (w-1, h-1).

### Robot Motion Rules
* Each robot has a position inside the room. We'll represent the position using coordinates (x, y) which are floats satisfying 0 ≤ x < w and 0 ≤ y < h. In our program we'll use instances of the Position class to store these coordinates.
* A robot has a direction of motion. We'll represent the direction using an integer d satisfying 0 ≤ d < 360, which gives an angle in degrees.
* All robots move at the same speed s, a float, which is given and is constant throughout the simulation. Every time-step, a robot moves in its direction of motion by s units.
* If a robot detects that it will hit the wall within the time-step, that time step is instead spent picking a new direction at random. The robot will attempt to move in that direction on the next time step, until it reaches another wall.

### Termination
The simulation ends when a specified fraction of the tiles in the room have been cleaned.

## Getting Started

### Pre-requisites and Local Development
Developers using this project should already have Python3 and pip installed on their local machines.

From the roomba-simulator folder run `pip install -r requirements.txt`. All required packages are included in the requirements file.

### Project Structure
```
├── roomba-simulator/
    ├── app.py
    ├── plot.py
    ├── ps2_visualize.py
    ├── verify_movement35.pyc
    ├── verify_movement36.pyc
    ├── verify_movement37.pyc
    ├── verify_movement38.pyc
```
This is structure has six files:
* *app.py* contains the robot models and the simulation function.
* *plot.py* contains functions for plotting data.
* *ps2_visualize.py* visualizes the robot's movement.
* *verify_movement35.pyc* is a precompiled module for Python 3.5 that assists with the visualization code.
* *verify_movement36.pyc* is a precompiled module for Python 3.6 that assists with the visualization code.
* *verify_movement37.pyc* is a precompiled module for Python 3.7 that assists with the visualization code.
* *verify_movement38.pyc* is a precompiled module for Python 3.8 that assists with the visualization code.

## Robotic Agents

In app.py we provide the `Robot` class, which stores the position and direction of a robot. Within this class, we provide methods that perform the following operations:

* Initializing the object
* Accessing the robot's position
* Accessing the robot's direction
* Setting the robot's position
* Setting the robot's direction

>Note: The `Robot` class is an abstract class, which means that we will never make an instance of it. Read up on the Python docs on abstract classes at this [link](https://docs.python.org/3/library/abc.html) and if you want more examples on abstract classes, follow this [link](https://julien.danjou.info/guide-python-static-class-abstract-methods/).

In the final implementation of `Robot`, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method `updatePositionAndClean()`.

Each robot must also have some code that tells it how to move about a room, which will go in a method called `updatePositionAndClean`.

Ordinarily we would consider putting all the robot's methods in a single class. However, we will consider robots with alternate movement strategies, to be implemented as different classes with the same interface. These classes will have a different implementation of `updatePositionAndClean` but are for the most part the same as the original robots. Therefore, we'd like to use inheritance to reduce the amount of duplicated code.

### Standard Robot

A `StandardRobot` is a robot with the standard movement strategy.
At each time-step, a `StandardRobot` attempts to move in its current direction; when it hits a wall, it chooses a new direction randomly.

### Random Walk Robot

A `RandomWalkRobot` is a robot with the "random walk" movement strategy. It chooses a new direction at random at the end of each time-step.

### Least Distance Robot

A `LeastDistanceRobot` is a robot with a smart movement strategy. Rather than choosing a random direction (angle) at each time-step, it searches for the nearest dirty tile relative to its position and sets its movevment direction based on that.

>Note: Comparisons between these different strategies can be found in the jupyter notebook `Notebook.ipynb`

## Running Animated Visualizations
>Note: This part is optional. It is cool and very easy to do, and may also be useful for debugging.

### Steps
We've provided some code to generate animations of your robots as they go about cleaning a room. These animations can also help you debug your simulation by helping you to visually determine when things are going wrong.

Here's how to run the visualization:

* In your simulation, at the beginning of a trial, insert the following code to start an animation:
```
    anim = ps2_visualize.RobotVisualization(num_robots, width, height)
```
(Pass in parameters appropriate to the trial, of course.) This will open a new window to display the animation and draw a picture of the room.

* Then, during each time-step, before the robot(s) move, insert the following code to draw a new frame of the animation:
```
    anim.update(room, robots)
```
where room is a RectangularRoom object and robots is a list of Robot objects representing the current state of the room and the robots in the room.

* When the trial is over, call the following method:
```
    anim.done()
```

>Note: We have done the previous steps for you :). You will only want to uncomment the specified lines found in app.py -> runSimulation()!

### Caution
The visualization code slows down your simulation so that the animation doesn't zip by too fast (by default, it shows 5 time-steps every second). Naturally, you will want to avoid running the animation code if you are trying to run many trials at once (for example, when you are running the full simulation).

For purposes of debugging your simulation, you can slow down the animation even further. You can do this by changing the call to RobotVisualization, as follows:
```
    anim = ps2_visualize.RobotVisualization(num_robots, width, height, delay)
```
The parameter delay specifies how many seconds the program should pause between frames. The default is 0.2 (that is, 5 frames per second). You can increase this value to make the animation slower or decrease it (0.01 is reasonable) to see many robots cleaning the room at a faster frame rate.

### Result
The resulting animation will look like this:

![Alt Text](https://media3.giphy.com/media/dEGoNojIKG6eke34ZZ/giphy.gif)

## Plotting
In plot.py we provide some cool plotting functions, make sure to play around with them or even write your own!

## Contributors
Ahmed Yasser<br>
Moaz Samy<br>
Osama Mohammed<br>
Osama Yasser


