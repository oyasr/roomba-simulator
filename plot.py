import math
import pylab
from app import StandardRobot, LeastDistanceRobot, RandomWalkRobot, runSimulation


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

# CoverageWasteRatio('Coverage Percent & Size Relation',
#                   'Dim length', 'Waste to Time Ratio', 5, LeastDistanceRobot)

# CostQualityTime("CostQualityTime", "Number of robots",
#                 "Time", 10, LeastDistanceRobot)

# NumOfBotWasteRatio('Waste & Size Relation', 'Dim length', 'Waste to Time Ratio')


# NumOfBotSizeWasteRatio('Waste & Size & Num of bots Relation\n LeastDistanceRobot',
#                        'Time', ' Waste to Time Ratio', 20)

# AspectRatioTimePlot('Test', 'Aspect Ratio', 'Time', 1, 100)

# AspectWasteRatioPlot("AspectRatio & WasteRatio",
#                      "AspectRatio", "WasteRatio", 1, 100)
