import math
import random
import ps2_visualize
from verify_movement38 import testRobotMovement

# Comment/uncomment the relevant lines, depending on your Python version

# For Python 3.5:
# from verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5

# For Python 3.6:
# from verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6

# For Python 3.7:
# from verify_movement37 import testRobotMovement
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

    def getTargetAngle(self, pos, target):
        """
        Computes and returns an angle based on the robot's position and 
        the targeted tile coordinates.

        Does NOT test whether the returned position fits inside the room.

        pos: tuple representing the robot's current x and y coordinates
        target: tuple representing the target's x and y coordinates

        Returns: float representing the angle in degrees, 0 <= angle < 360
        """
        sidex = target[0] - int(pos[0])
        sidey = target[1] - int(pos[1])
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
        try:

            # Clean the tile if it is not clean
            if not self.tiles[y][x]:
                self.tiles[y][x] = True
                self.clean_tiles += 1
                return None
            else:
                return 1

        # Handle tile outside room
        except IndexError:
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
        except IndexError:
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

    def nearestDirtyTile(self, pos, z=1):
        """
        Returns the nearest dirty tile relative to the robot's current possition,
        and returns none if the room is clean.

        pos: tuple representing the robot's current x and y coordinates

        Returns: tuple representing the x and y coordinates of the nearest dirty tile
        """
        x, y = pos

        # Index range of left bound tiles
        def leftBound(self):
            for i in range(y-z+1, y+z):
                if self.height > i >= 0 and self.width > (x-z) >= 0:
                    if not self.isTileCleaned(x-z, i):
                        return (x-z, i)

        # Index range of right bound tiles
        def rightBound(self):
            for i in range(y-z+1, y+z):
                if self.height > i >= 0 and self.width > (x+z) >= 0:
                    if not self.isTileCleaned(x+z, i):
                        return (x+z, i)

        # Index range of upper bound tiles
        def upperBound(self):
            for i in range(x-z, x+z+1):
                if self.width > i >= 0 and self.height > (y-z) >= 0:
                    if not self.isTileCleaned(i, y-z):
                        return(i, y-z)

        # Index range of lower bound tiles
        def lowerBound(self):
            for i in range(x-z, x+z+1):
                if self.width > i >= 0 and self.height > (y+z) >= 0:
                    if not self.isTileCleaned(i, y+z):
                        return (i, y+z)

        # Shuffle the searching order
        bounds = [rightBound, leftBound, lowerBound, upperBound]
        random.shuffle(bounds)
        for bound in bounds:
            if bound(self) is not None:
                return bound(self)

        # Increase the search diameter
        z += 1
        if z < self.width or z < self.height:
            return self.nearestDirtyTile(pos, z)


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
            if self.room.cleanTileAtPosition(position) is not None:
                return 1

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
    trials_waste = []

    for i in range(num_trials):
        # anim = ps2_visualize.RobotVisualization(
        #    num_robots, width, height, 0.3)

        # Set room & robots list
        wasted_ticks = []
        robots = []
        room = RectangularRoom(width, height)
        room_size = room.getNumTiles()

        # Initialize robots
        for j in range(num_robots):

            # Create instance & add to list
            robot = robot_type(room, speed)
            robots.append(robot)
            wasted_ticks.append(-1)

        # Do until room is clean
        clock_tick = 0
        while room.getNumCleanedTiles() < (min_coverage * room_size):
            # anim.update(room, robots)

            # Move each robot
            for robot in range(len(robots)):
                if robots[robot].updatePositionAndClean() is not None:
                    wasted_ticks[robot] += 1
            clock_tick += 1
        trials_waste.append(sum(wasted_ticks)/len(wasted_ticks))
        # Add trial result
        trials.append(clock_tick)
    # anim.update(room, robots)
    # anim.done()
    # Return average
    return ((sum(trials) / len(trials)), (sum(trials_waste)/len(trials_waste)))


# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(3, 1, 10, 10, 1, 1, StandardRobot))



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

            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)


            if self.room.cleanTileAtPosition(position) is not None:
                return 1

            
        # The position is out of the room
        else:
            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)


# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(5, 1, 10, 10, 1, 300, RandomWalkRobot))
# testRobotMovement(RandomWalkRobot, RectangularRoom)


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

        # Targets nearest dirty tile coordinates
        target = self.room.nearestDirtyTile(Pos)
        if target is not None:

            # Sets the robot angle if target exist
            angle = self.position.getTargetAngle(Pos, target)
            self.setRobotDirection(float(angle))

        # Update position & clean
        self.setRobotPosition(position)
        if self.room.cleanTileAtPosition(position) is not None:
            return 1


# print("least (Time, avgWastePerBot)", runSimulation(
#     1, 1, 7, 7, 1, 1, LeastDistanceRobot))
# testRobotMovement(leastdistanceRobot, RectangularRoom)
# print(runSimulation(2, 1, 10, 10, 1, 1, LeastDistanceRobot))
