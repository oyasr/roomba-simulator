import math
import pylab
import random
import ps2_visualize


# Comment/uncomment the relevant lines, depending on your Python version

# For Python 3.5:
# from verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5

# For Python 3.6:
# from verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6

# For Python 3.7:
from verify_movement37 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)

    def ReLocateAngle(self, Pos, target):
        """
         Computes and returns an angle base on robot's position and  targeted tile coordinates'

        Parameters
        ----------
        Pos : tuple
            robot x, y coordinates.
        target : tuple
            targeted tile x, y coordinates.

        Returns
        -------
        angle : float
            sets the robot's angle to reach the target.

        """
        sidex = target[0] - int(Pos[0])
        sidey = target[1] - int(Pos[1])
        if sidex == 0:
            if sidey > 0:
                angle = 0
            else:
                angle = 180
        elif sidey == 0:
            if sidex > 0:
                angle = 90
            else:
                angle = 270
        else:
            if sidex > 0:
                angle = math.atan(abs(sidey/sidex))*180/math.pi
                if sidey > 0:
                    angle = 90-angle
                else:
                    angle = 90 + angle
            else:
                angle = math.atan(abs(sidex/sidey))*180/math.pi
                if sidey < 0:
                    angle += 180
                else:
                    angle = 360-angle
        return angle


# === Problem 1


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.clean_tiles = 0
        self.tiles = [[False for j in range(width)] for i in range(height)]

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # Get the coordinates of the tile
        x, y = int(pos.getX()), int(pos.getY())

        # Try to clean the tile
        try:

            # Clean the tile if it is not clean
            if not self.tiles[y][x]:
                self.tiles[y][x] = True
                self.clean_tiles += 1

        # Handle tile outside room
        except IndexError as e:
            pass

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # Try to access tile
        try:
            return self.tiles[n][m]
        # Handle tile outside room
        except IndexError as e:
            pass

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return self.clean_tiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        # Generate random coordinates
        x = float(random.randrange(0, self.width))
        y = float(random.randrange(0, self.height))
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # Get coordinates
        x, y = pos.getX(), pos.getY()

        if x >= self.width or y >= self.height:
            return False
        if x < 0 or y < 0:
            return False

        return True

    def nearestDirtyTile(self, Pos, z=1):
        """
        searches for the nearest dirty tile by iterating through the robot position border 
        in Tiles array and increase the border distance if the current border is clean 
        returns the coordinates of the nearest dirty tile & None if all tiles are clean.
        


        Parameters
        ----------
        Pos : tuple
            robot x, y coordinates.
        z : int, optional
            border distance from robot position. starts with vaule of 1

        Returns
        -------
        tuple
            nearest dirty tile coordinates.
        None
            if all tiles are clean.

        """
        #maps the position to x, y  variables
        x, y = Pos[0], Pos[1]
        
        # left bound elements
        def leftBound(self):
            for i in range(y-z+1, y+z):
                if self.height > i >= 0 and self.width > (x-z) >= 0:
                    if not self.isTileCleaned(x-z, i):
                        return (x-z, i)
                    
        # right bound elements
        def rightBound(self):
            for i in range(y-z+1, y+z):
                if self.height > i >= 0 and self.width > (x+z) >= 0:
                    if not self.isTileCleaned(x+z, i):
                        return (x+z, i)
                    
        # upper bound elements            
        def upperBound(self):
            for i in range(x-z, x+z+1):
                if self.width > i >= 0 and self.height > (y-z) >= 0:
                    if not self.isTileCleaned(i, y-z):
                        return(i, y-z)
                    
        # lower bound elements
        def lowerBound(self):
            for i in range(x-z, x+z+1):
                if self.width > i >= 0 and self.height > (y+z) >= 0:
                    if not self.isTileCleaned(i, y+z):
                        return (i, y+z)
                    
        #randomize the sequnce of the border sides to increase multi robots case performance
        bounds = [rightBound, leftBound, lowerBound, upperBound]
        random.shuffle(bounds)
        for bound in bounds:
            if bound(self) is not None:
                return bound(self)
        
        #increase the border distance
        z += 1
        if z < self.width or z < self.height:
            return self.nearestDirtyTile(Pos, z)
# === Problem 2


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = float(random.choice([0, 90, 180, 360]))
        self.position = room.getRandomPosition()
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Get potential next position
        position = self.position.getNewPosition(self.direction, self.speed)

        # Check if position in room
        if self.room.isPositionInRoom(position):

            # Update position & clean
            self.setRobotPosition(position)
            self.room.cleanTileAtPosition(position)

        # The position is out of the room
        else:

            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    # Set trial results
    trials = []

    for i in range(num_trials):
        anim = ps2_visualize.RobotVisualization(num_robots, width, height, 0.05)

        # Set room & robots list
        robots = []
        room = RectangularRoom(width, height)
        room_size = room.getNumTiles()

        # Initialize robots
        for j in range(num_robots):

            # Create instance & add to list
            robot = robot_type(room, speed)
            robots.append(robot)

        # Do until room is clean
        clock_tick = 0
        while room.getNumCleanedTiles() < (min_coverage * room_size):
            anim.update(room, robots)

            # Move each robot
            for robot in robots:
                robot.updatePositionAndClean()
            clock_tick += 1

        # Add trial result
        trials.append(clock_tick)
    anim.update(room, robots)
    anim.done()
    # Return average

    return sum(trials) / len(trials)


# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1, 5, 5, 1, 1, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Get potential next position
        position = self.position.getNewPosition(self.direction, self.speed)

        # Check if position in room
        if self.room.isPositionInRoom(position):

            # Update position & clean
            self.setRobotPosition(position)
            self.room.cleanTileAtPosition(position)

            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)

        # The position is out of the room
        else:
            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)

            self.setRobotPosition(position)
            self.room.cleanTileAtPosition(position)

# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(5, 1, 10, 10, 1, 300, RandomWalkRobot))


class LeastDistanceRobot(Robot):
    """
    A LeastDistanceRobot is a Robot with the distance based movement strategy.

    At each time-step, a LeastDistanceRobot looks for nearest dirty 
    tile to it's position and updates it's angle to get to it .
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        # Get potential next position
        position = self.position.getNewPosition(self.direction, self.speed)
        Pos = (int(position.getX()), int(position.getY()))
        
        # targets nearest dirty tile coordinates
        target = self.room.nearestDirtyTile(Pos)
        if target is not None:
            
            #sets the robot angle if target exist
            angle = self.position.ReLocateAngle(Pos, target)
            self.setRobotDirection(float(angle))
            
        # Update position & clean
        self.setRobotPosition(position)
        self.room.cleanTileAtPosition(position)


print("least", runSimulation(10, 1, 30, 30, 1, 1, LeastDistanceRobot))
# testRobotMovement(leastdistanceRobot, RectangularRoom)


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0,
                                    20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0,
                                    20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:",
              width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(
            2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(
            2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# === Problem 6
# NOTE: If you are running the simulation, you will have to close it
# before the plot will show up.


# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
# showPlot1('Test', 'Number of robots', 'Time')


#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
# showPlot2('Test', 'Time', 'Aspect Ration')
