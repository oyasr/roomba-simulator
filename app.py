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
            else:
                return 1
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
        # maps the position to x, y  variables
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

        # randomize the sequnce of the border sides to increase multi robots case performance
        bounds = [rightBound, leftBound, lowerBound, upperBound]
        random.shuffle(bounds)
        for bound in bounds:
            if bound(self) is not None:
                return bound(self)

        # increase the border distance
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
        #     num_robots, width, height, 0.2)

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
            if self.room.cleanTileAtPosition(position) is not None:
                return 1

            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)

        # The position is out of the room
        else:
            # Update angle
            angle = float(random.randint(0, 360))
            self.setRobotDirection(angle)


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

            # sets the robot angle if target exist
            angle = self.position.ReLocateAngle(Pos, target)
            self.setRobotDirection(float(angle))

        # Update position & clean
        self.setRobotPosition(position)
        if self.room.cleanTileAtPosition(position) is not None:
            return 1


# print("least (Time, avgWastePerBot)", runSimulation(
#     1, 1, 7, 7, 1, 1, LeastDistanceRobot))
# testRobotMovement(leastdistanceRobot, RectangularRoom)


def TimeNumberPlot(title, x_label, y_label, dim_length):
    """
    Plots Number of robots & Time relation for each robot type
    """
    num_robot_range = range(1, 11)
    times1, times2, times3 = ([] for i in range(3))
    time_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    for i in range(len(Robots)):
        for num_robots in num_robot_range:
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, 1, 5, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(num_robot_range, time)
    pylab.title(title+"\n for size of {0}x{0}".format(dim_length))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def AspectRatioTimePlot(title, x_label, y_label, num_robots, area):
    """
    plots the relation between aspect ratio and
     it's impact on time for each robot type
    """
    aspect_ratios = []
    times1, times2, times3 = ([] for i in range(3))
    time_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    start = math.sqrt(area)
    aspect_dim_list = []
    for dim in range(1, 11):
        aspect_dim_list.append(start*dim)
    for width in aspect_dim_list:
        height = area / width
        aspect_ratios.append("1 : {0}".format(int(width/height)))
        for i in range(len(Robots)):
            result = runSimulation(
                num_robots, 1.0, int(width), int(height), 1, 20, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(aspect_ratios, time)

    pylab.title(
        title+"\n for {0} Robots & Area of {1}".format(num_robots, area))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def AspectWasteRatioPlot(title, x_label, y_label, num_robots, area):
    """
    plots the relation between aspect ratio and
     it's impact on time for each robot type
    """
    aspect_ratios = []
    times1, times2, times3 = ([] for i in range(3))
    waste_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    start = math.sqrt(area)
    aspect_dim_list = []
    for dim in range(1, 11):
        aspect_dim_list.append(start*dim)
    for width in aspect_dim_list:
        height = area / width
        aspect_ratios.append("1 : {0}".format(int(width/height)))
        for i in range(len(Robots)):
            result = runSimulation(
                num_robots, 1.0, int(width), int(height), 1, 20, Robots[i])
            waste_Robot_list[i].append(result[1]/result[0])
    for time in waste_Robot_list:
        pylab.plot(aspect_ratios, time)

    pylab.title(
        title+"\n for {0} Robots & Area of {1}".format(num_robots, area))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def EfficiencyPlot(title, x_label, y_label, num_robots):
    """
    Plots size & Time relation for each robot type (Efficiency)

    LeastDistanceRobot is x7 effient that standard
    """
    dim_length_range = range(5, 31, 5)
    times1, times2, times3 = ([] for i in range(3))
    time_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    for i in range(len(Robots)):
        for dim_length in dim_length_range:
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, 1, 20, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(dim_length_range, time)
    pylab.title(title+"\n for {0} Robots".format(num_robots))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def ConsistencyPlot(title, x_label, y_label, dim_length, num_robots):
    """
    Plots trt number & Time Relation for each robot type
    Consistency differance
    to Caculate Varince and Standard Deviation
    """
    try_num_range = range(16)
    times1, times2, times3 = ([] for i in range(3))
    time_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    for i in range(len(Robots)):
        for try_num in try_num_range:
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, 1, 1, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(try_num_range, time)
    pylab.title(
        title+"\n for size of {0}x{0} & {1} Robots".format(dim_length, num_robots))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def CoverageRate(title, x_label, y_label, num_robots, robot_type):
    """
    What information does the plot produced by this function tell you?
    efficiency
    """
    dim_length_range = range(5, 31, 5)
    coverage_percent_range = range(70, 105, 5)
    coverage_percent_range = [i/100 for i in coverage_percent_range]
    alist, blist, clist, dlist, elist, flist, glist = ([] for i in range(7))
    coverage_percent_list = [alist, blist, clist, dlist, elist, flist, glist]
    for dim_length in dim_length_range:
        for i in range(len(coverage_percent_range)):
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, coverage_percent_range[i], 20, robot_type)
            coverage_percent_list[i].append(result[0])

    for percentlist in coverage_percent_list:
        pylab.plot(dim_length_range, percentlist)

    pylab.title(
        title+"\n for {0} bots of {1} Type ".format(num_robots, str(robot_type)))
    pylab.legend(("0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1.0"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def CoverageWasteRatio(title, x_label, y_label, num_robots, robot_type):
    """
    efficiency
    """
    dim_length_range = range(5, 31, 5)
    coverage_percent_range = range(70, 105, 5)
    coverage_percent_range = [i/100 for i in coverage_percent_range]
    alist, blist, clist, dlist, elist, flist, glist = ([] for i in range(7))
    coverage_percent_list = [alist, blist, clist, dlist, elist, flist, glist]
    for dim_length in dim_length_range:
        for i in range(len(coverage_percent_range)):
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, coverage_percent_range[i], 50, robot_type)
            coverage_percent_list[i].append(result[1]/result[0])

    for percentlist in coverage_percent_list:
        pylab.plot(dim_length_range, percentlist)

    pylab.title(
        title+"\n for {0} bots of {1} Type ".format(num_robots, str(robot_type)))
    pylab.legend(("0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1.0"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def CostQualityTime(title, x_label, y_label, dim_length, robot_type):
    """
    What information does the plot produced by this function tell you?
    efficiency
    """
    # dim_length_range = range(5, 31, 5)
    num_robot_range = range(1, 11)
    coverage_percent_range = range(70, 105, 5)
    coverage_percent_range = [i/100 for i in coverage_percent_range]
    alist, blist, clist, dlist, elist, flist, glist = ([] for i in range(7))
    coverage_percent_list = [alist, blist, clist, dlist, elist, flist, glist]
    for num_robots in num_robot_range:
        for i in range(len(coverage_percent_range)):
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, coverage_percent_range[i], 20, robot_type)
            coverage_percent_list[i].append(result[0])

    for percentlist in coverage_percent_list:
        pylab.plot(num_robot_range, percentlist)

    pylab.title(
        title+"\n for {0} bots of {1} Type ".format(num_robots, str(robot_type)))
    pylab.legend(("0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1.0"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def NumOfBotWasteRatio(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    waste on average with num on bots
    to find the sweet spot for this room another function must be madfe with
    """
    alist, blist, clist, dlist, elist = ([] for i in range(5))
    num_robots_list = [alist, blist, clist, dlist, elist]
    t1list, t2list, t3list, t4list, t5list = ([] for i in range(5))
    time_robots_list = [t1list, t2list, t3list, t4list, t5list]
    dim_length_range = range(10, 51, 5)
    num_robots_range = range(5, 26, 5)
    for dim_length in dim_length_range:
        for i in range(len(num_robots_list)):
            results = runSimulation(
                num_robots_range[i], 1.0, dim_length, dim_length, 1, 20, LeastDistanceRobot)
            num_robots_list[i].append(results[1]/results[0])
            time_robots_list[i].append(results[0])

    for i in range(len(num_robots_range)):
        pylab.plot(dim_length_range, num_robots_list[i])
    pylab.title(title)
    pylab.legend(('5', '10', "15", "20", "25"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    # === Problem 6
# NOTE: If you are running the simulation, you will have to close it
# before the plot will show up.


def NumOfBotSizeWasteRatio(title, x_label, y_label, dim_length):
    """
    What information does the plot produced by this function tell you?
    waste on average with num on bots
    to find the sweet spot for this room another function must be madfe with
    """
    alist, blist, clist, dlist, elist = ([] for i in range(5))
    num_robots_list = [alist, blist, clist, dlist, elist]
    t1list, t2list, t3list, t4list, t5list = ([] for i in range(5))
    time_robots_list = [t1list, t2list, t3list, t4list, t5list]
    num_robots_range = range(5, 26, 5)

    for i in range(len(num_robots_list)):
        results = runSimulation(
            num_robots_range[i], 1.0, dim_length, dim_length, 1, 100, LeastDistanceRobot)
        num_robots_list[i].append(results[1]/results[0])
        time_robots_list[i].append(results[0])

    for i in range(len(num_robots_list)):
        pylab.scatter(time_robots_list[i], num_robots_list[i], s=100)
    pylab.title(title)
    pylab.legend(('5', '10', "15", "20", "25"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# Plots


# TimeNumberPlot('Number of robots & Time relation',
#                'Number of robots', 'Time (Tick)', 20)

# EfficiencyPlot("Time & Size Relation (Efficiency)", "Dim length", "Time", 1)

# ConsistencyPlot("Consistency", "Try number", "Time", 20, 1)

# CoverageRate('Coverage Percent & Size Relation',
#              'Dim length', 'Time', 1, RandomWalkRobot)

CoverageWasteRatio('Coverage Percent & Size Relation',
                   'Dim length', 'Waste to Time Ratio', 5, LeastDistanceRobot)

# CostQualityTime("CostQualityTime", "Number of robots",
#                 "Time", 10, LeastDistanceRobot)

# NumOfBotWasteRatio('Waste & Size Relation', 'Dim length', 'Waste to Time Ratio')


# NumOfBotSizeWasteRatio('Waste & Size & Num of bots Relation\n LeastDistanceRobot',
#                        'Time', ' Waste to Time Ratio', 20)

# AspectRatioTimePlot('Test', 'Aspect Ratio', 'Time', 1, 100)

# AspectWasteRatioPlot("AspectRatio & WasteRatio",
#                      "AspectRatio", "WasteRatio", 1, 100)
