"""
    This is a simple implementation of
    the A* algorithm. It utilizes a dictionary
    mapping node indices to MapNode(s).
    The final path is found by going up
    the parent tree.
"""

from math import sqrt

"""
    This class is a simple data
    structure to represent the information
    needed in a node on the map.
"""
class MapNode():
    def __init__(self, key=None, cost=None, coordinate=None, roads=None, parent=None):
        self.key = key
        self.cost = cost
        self.coordinate = coordinate
        self.roads = roads
        self.parent = parent

"""
    This function assumes that points
    are in the form of a tuple, accessible
    by indicies 0 and 1, where 0 is the
    x coordinate, and 1 is the y coordinate

    The distance formula is:
    square root of (x1-x2) squared + (y1-y2) squared
"""
def calculate_distance(point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    dx = x1-x2
    p_dx = pow(dx, 2)

    y1 = point1[1]
    y2 = point2[1]
    dy = y1-y2
    p_dy = pow(dy, 2)

    sum_pdx_pdy = p_dx + p_dy
    return sqrt(sum_pdx_pdy)


"""
    The cost formula is f = g + h, where g is path cost 
    and h is heuristic. The heuristic used is the output of 
    the Pythagorean distance formula.
"""
def calcluate_cost(parent_node, child_node):
    g = parent_node.cost
    h = calculate_distance(parent_node.coordinate, child_node.coordinate)
    return g + h

def get_smallest_node_index(queue):
    minimum_index = 0
    for i, node in enumerate(queue):
        minimum = queue[minimum_index]
        if node.cost < minimum.cost:
            minimum_index = i
    return minimum_index

def in_queue(queue, node_index):
    for item in queue:
        if item.key == node_index:
            return item
    return None

"""
    This function build a cost dictionary
    where the key is the node number and the
    value is a MapNode object with all the
    costs.
"""
def build_cost_dict(M, start, goal):
    # Initialize the queue. This is the frontier
    queue = [MapNode(key=start, cost=0, coordinate=M.intersections[start], roads=M.roads[start], parent=None)]

    # Keep track of explored nodes. O(1) lookup
    explored = {}

    # Map each node to a cost. O(1) lookup
    # This dictionary will eventually have one path
    #   this is optimal
    node_costs = {}

    while len(queue) > 0:
        # Pop out the node with the smallest cost
        smallest_node_index = get_smallest_node_index(queue)
        parent_node = queue.pop(smallest_node_index)

        # Mark node as explored
        explored[parent_node.key] = parent_node

        # Add children to the queue with cost and parent mapped
        for child in parent_node.roads:
            # Check if child is in queue
            child_in_queue = in_queue(queue, child)

            if child not in explored and not child_in_queue:
                child_node = MapNode(key=child, coordinate=M.intersections[child], roads=M.roads[child], parent=parent_node.key)
                child_node.cost = calcluate_cost(parent_node, child_node)
                queue.append(child_node)

            # Handle case if child is in the queue
            # For this case we want to update the cost if that path
            #   is cheaper than with the previous parent
            elif child not in explored and child_in_queue:
                potential_cost = calcluate_cost(parent_node, child_in_queue)
                if potential_cost < child_in_queue.cost:
                    child_in_queue.cost = potential_cost
                    child_in_queue.parent = parent_node.key

        # Add the parent_node to the node_costs dict
        node_costs[parent_node.key] = parent_node

    return node_costs

def get_path(node_costs, goal):
    path = []
    node = node_costs[goal]
    while node is not None:
        path.append(node.key)
        if node.parent is None:
            break
        node = node_costs[node.parent]
    path.reverse()
    return path

"""
    The shortest_path function relies
    on the cost dictionary to be built.
    Once the dictionary is built, the path can
    be found by going up the tree starting
    with the goal.
"""
def shortest_path(M,start,goal):
    node_costs = build_cost_dict(M, start, goal)
    return get_path(node_costs, goal)

#-----------------------------------------------------

"""
    TESTING SECTION
"""
class TestMapImpl():
    def __init__(self):
        self.intersections = None
        self.roads = None

def tests():
    M = TestMapImpl()

    # Data taken from workbook
    M.intersections = {0: [0.7798606835438107, 0.6922727646627362],
                        1: [0.7647837074641568, 0.3252670836724646],
                        2: [0.7155217893995438, 0.20026498027300055],
                        3: [0.7076566826610747, 0.3278339270610988],
                        4: [0.8325506249953353, 0.02310946309985762],
                        5: [0.49016747075266875, 0.5464878695400415],
                        6: [0.8820353070895344, 0.6791919587749445],
                        7: [0.46247219371675075, 0.6258061621642713],
                        8: [0.11622158839385677, 0.11236327488812581],
                        9: [0.1285377678230034, 0.3285840695698353]}
    M.roads = [[7, 6, 5],
                [4, 3, 2],
                [4, 3, 1],
                [5, 4, 1, 2],
                [1, 2, 3],
                [7, 0, 3],
                [0],
                [0, 5],
                [9],
                [8]]

    print(shortest_path(M, 0 ,0))

if __name__ == '__main__':
    tests()