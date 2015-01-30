__author__ = 'colemanjackson'
import json
import sys
from pprint import pprint


#Contains the default information about the forest about to be parsed
class ForestInfo(object):

    #initalize with default info
    #parse_info:JSON Tree Object
    def __init__(self, parse_info):
        self.forest_depth = int(parse_info["right"])
        print "Forest Depth = " + str(self.forest_depth)
        self.left = int(parse_info["left"])
        self.right = int(parse_info["right"])
        self.name = parse_info["name"]
        self.id = int(parse_info["forest_id"])
        self.active_node_count = [1] * self.forest_depth

    # Node object of format { "f":int, "l":int, "anc":int } expected

    def update_active_node(self, json_node_info, forest_info):
        print "Updating Forest Info: Active Nodes: " + str(forest_info.active_node_count)
        level = int(json_node_info["l"])
        self.active_node_count[level - 1] = self.active_node_count[level-1] + int(json_node_info["anc"])



def main():
    first_time = True
    forest_info = None
    print "Logging: Started Main"
    print "Reading from stdin:"

    for line in sys.stdin:

        #Null Check
        if line is None:
            continue

        #On First Time through, create object tree
        if first_time:
            JSON_Tree_Info = json.loads(line)
            forest_info = ForestInfo(JSON_Tree_Info)
            first_time = False
            continue

        #Update Active Nodes
        print "updating node information at line " + line
        node_info = json.loads(line)
        forest_info.update_active_node(node_info, forest_info)

    #Final Display
    print "Final Forest Info: Active Nodes: " + str(forest_info.active_node_count)
    print "Final Forest Info: Forest Depth: " + str(forest_info.forest_depth)
    print "Final Forest Info: Forest Left: " + str(forest_info.left)
    print "Final Forest Info: Forest right: " + str(forest_info.right)
    print "Final Forest Info: Forest Left: " + str(forest_info.left)

#execute block
main()