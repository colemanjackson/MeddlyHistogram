__author__ = 'colemanjackson'
import json
import sys
import matplotlib.pyplot as plt
import numpy as np

# Contains the default information about the forest about to be parsed
class ForestInfo(object):
    # initalize with default info
    # parse_info:JSON Tree Object
    def __init__(self, parse_info):
        self.forest_depth = int(parse_info["right"])
        print "Forest Depth = " + str(self.forest_depth)
        self.left = int(parse_info["left"])
        self.right = int(parse_info["right"])
        self.name = parse_info["name"]
        self.id = int(parse_info["forest_id"])
        self.active_node_count = [1] * self.forest_depth

    # Node object of format { "f":int, "l":int, "anc":int } expected
    # rects should be a bargraph object from matplotlib,
    # refer to http://stackoverflow.com/questions/16249466/dynamically-updating-a-bar-plot-in-matplotlib for example
    def update_active_node(self, json_node_info, forest_info, rects):
        print "Updating Forest Info: Active Nodes: " + str(forest_info.active_node_count)
        level = int(json_node_info["l"])
        self.active_node_count[level - 1] = self.active_node_count[level - 1] + int(json_node_info["anc"])
        rects[level - 1].set_height(self.active_node_count[level - 1])


# Simple Logging Object to log events in program execution
class Logger(object):

    def __init__(self):
        pass

    @staticmethod
    def log_begin_message(self):
        print "Logging: Started Main"
        print "Reading from stdin:"

    @staticmethod
    def log_final_output(self, forest_info):
        print "Final Forest Info: Active Nodes: " + str(forest_info.active_node_count)
        print "Final Forest Info: Forest Depth: " + str(forest_info.forest_depth)
        print "Final Forest Info: Forest Left: " + str(forest_info.left)
        print "Final Forest Info: Forest right: " + str(forest_info.right)
        print "Final Forest Info: Forest Left: " + str(forest_info.left)

    @staticmethod
    def log_line_update(self, line):
        print "updating node information at line " + line


def animate_bar_plot():
    first_time = True
    forest_info = None
    log = Logger()

    log.log_begin_message()
    for line in sys.stdin:
        # Null Check
        if line is None:
            continue

        # On First Time through, create object tree
        if first_time:
            JSON_Tree_Info = json.loads(line)
            forest_info = ForestInfo(JSON_Tree_Info)
            rects = plt.bar(range(forest_info.forest_depth), forest_info.active_node_count, align='center')
            first_time = False
            continue

        # Update Active Nodes
        log.log_line_update(line)
        node_info = json.loads(line)
        forest_info.update_active_node(node_info, forest_info, rects)
        fig.canvas.draw()

    # Final Display
    log.log_final_output(forest_info)


def setup_backend(backend='TkAgg'):
    import sys

    del sys.modules['matplotlib.backends']
    del sys.modules['matplotlib.pyplot']
    import matplotlib as mpl

    mpl.use(backend)  # do this before importing pyplot
    import matplotlib.pyplot as plt

    return plt


# execute block
plt = setup_backend()
fig = plt.figure()
win = fig.canvas.manager.window
win.after(3, animate_bar_plot)
plt.show()