import math
import pylab
from app import StandardRobot, LeastDistanceRobot, RandomWalkRobot, runSimulation


def timeNumberPlot(title, x_label, y_label, dim_length):
    """
    Plots the relation between the number of robots and the average time
    taken by different robots to clean a portion of the room.
    """
    num_robot_range = range(1, 11)
    times1, times2, times3 = ([] for i in range(3))
    time_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    for i in range(len(Robots)):
        for num_robots in num_robot_range:
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, 1, 100, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(num_robot_range, time)
    pylab.title(title+f"\n for room size of {dim_length}x{dim_length}")
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def timeAspectRatioPlot(title, x_label, y_label, area, num_robots):
    """
    Plots the relation between the area of a square room and the average and
    the average time taken by diffrent robots to clean a portion of th
    room.
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
                num_robots, 1.0, int(width), int(height), 1, 100, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(aspect_ratios, time)

    pylab.title(
        title+f"\n for {num_robots} Robots & Area of {area}")
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def wasteAspectRatioPlot(title, x_label, y_label, num_robots, area):
    """
    Plots the relation between room's aspect ratio and the waste percentage
    for each robot.
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
                num_robots, 1.0, int(width), int(height), 1, 100, Robots[i])
            waste_Robot_list[i].append(result[1]/result[0])
    for time in waste_Robot_list:
        pylab.plot(aspect_ratios, time)

    pylab.title(
        title+"\n for {0} Robots & Area of {1}".format(num_robots, area))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def timeAreaPlot(title, x_label, y_label, num_robots):
    """
    Plots the relation between the area of a room and the average time
    taken by different robots to clean a certain portion of that room.
    """
    dim_length_range = range(5, 31, 5)
    times1, times2, times3 = ([] for i in range(3))
    time_Robot_list = [times1, times2, times3]
    Robots = [StandardRobot, LeastDistanceRobot, RandomWalkRobot]
    for i in range(len(Robots)):
        for dim_length in dim_length_range:
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length, 1, 100, Robots[i])
            time_Robot_list[i].append(result[0])
    for time in time_Robot_list:
        pylab.plot(dim_length_range, time)
    pylab.title(title+"\n for {0} Robots".format(num_robots))
    pylab.legend(('StandardRobot', 'LeastDistanceRobot', "RandomWalkRobot"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def consistencyPlot(title, x_label, y_label, dim_length, num_robots):
    """
    Performs the same exact experiment multiple of times
    for a robot or a number of robots and plots the outcomes of
    these experiments in terms of time taken for each individual
    experiment to measure the consistency of performance for various robots.
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


def timeAreaPortionPlot(title, x_label, y_label, num_robots, robot_type):
    """
    Plots the relation between the area of square room and the average
    time taken by a robot to clean a specific portion of the room,
    (Different portions are plotted)
    """
    dim_length_range = range(5, 31, 5)
    coverage_percent_range = range(70, 105, 5)
    coverage_percent_range = [i/100 for i in coverage_percent_range]
    alist, blist, clist, dlist, elist, flist, glist = ([] for i in range(7))
    coverage_percent_list = [alist, blist, clist, dlist, elist, flist, glist]
    for dim_length in dim_length_range:
        for i in range(len(coverage_percent_range)):
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length,
                coverage_percent_range[i], 100, robot_type)
            coverage_percent_list[i].append(result[0])

    for percentlist in coverage_percent_list:
        pylab.plot(dim_length_range, percentlist)

    pylab.title(
        title+f"\n for {num_robots} bots of {robot_type.__name__} type")
    pylab.legend(("0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1.0"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# Not sure about it
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
                num_robots, 1.0, dim_length, dim_length,
                coverage_percent_range[i], 100, robot_type)
            coverage_percent_list[i].append(result[1]/result[0])

    for percentlist in coverage_percent_list:
        pylab.plot(dim_length_range, percentlist)

    pylab.title(
        title+f"\n for {num_robots} bots of {robot_type.__name__} type")
    pylab.legend(("0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1.0"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def timeNumberPortionPlot(title, x_label, y_label, dim_length, robot_type):
    """
    Plots the relation between the number of robots and the average time
    taken to clean a certain portion of the room, 
    (each portion is plotted)
    """
    num_robot_range = range(1, 11)
    coverage_percent_range = range(70, 105, 5)
    coverage_percent_range = [i/100 for i in coverage_percent_range]
    alist, blist, clist, dlist, elist, flist, glist = ([] for i in range(7))
    coverage_percent_list = [alist, blist, clist, dlist, elist, flist, glist]
    for num_robots in num_robot_range:
        for i in range(len(coverage_percent_range)):
            result = runSimulation(
                num_robots, 1.0, dim_length, dim_length,
                coverage_percent_range[i], 100, robot_type)
            coverage_percent_list[i].append(result[0])

    for percentlist in coverage_percent_list:
        pylab.plot(num_robot_range, percentlist)

    pylab.title(
        title+f"\n for {num_robots} bots of {robot_type.__name__} type")
    pylab.legend(("0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1.0"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def wasteAreaNumberPlot(title, x_label, y_label):
    """
    Plots the relation between the waste percentage and the area of the
    room for a different number of robots,
    (each plotted individually)
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
                num_robots_range[i], 1.0, dim_length,
                dim_length, 1, 100, LeastDistanceRobot)
            num_robots_list[i].append(results[1]/results[0])
            time_robots_list[i].append(results[0])

    for i in range(len(num_robots_range)):
        pylab.plot(dim_length_range, num_robots_list[i])
    pylab.title(title)
    pylab.legend(('5', '10', "15", "20", "25"))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# Not sure about it
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
            num_robots_range[i], 1.0, dim_length, dim_length, 1, 50, LeastDistanceRobot)
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

# timeNumberPlot('Number of robots & Time relation',
#                'Number of robots', 'Time (Tick)', 20)

# timeAspectRatioPlot('Aspect Ratio & Time relation',
#                     'Room Aspect Ratio', 'Time', 100, 1)

# wasteAspectRatioPlot("AspectRatio & WasteRatio relation",
#                      "Room Aspect Ratio", "Waste Percentage", 1, 100)

# timeAreaPlot("Time & Room Area relation",
#              "Length (squared)", "Time", 1)

# consistencyPlot("Consistency", "Try number", "Time", 20, 1)

# timeAreaPortionPlot('Room Portion & Time relation',
#                     'Length (squared)', 'Time', 1, RandomWalkRobot)

# # CoverageWasteRatio('Coverage Percent & Size Relation','Length (squared)',
# #                    'Waste Percentage', 5, LeastDistanceRobot)

# timeNumberPortionPlot("CostQualityTime", "Number of robots",
#                       "Time", 10, LeastDistanceRobot)

# wasteAreaNumberPlot('Waste & Size Relation', 'Length (squared)',
#                     'Waste Percentage')


# # NumOfBotSizeWasteRatio('Waste & Size & Num of bots Relation\n LeastDistanceRobot',
# #                         'Time', ' Waste Percentage', 20)
