"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter


def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    firstline = True
    filez = open(file_path)
    truenumbers = []
    numbernodes = []
    for line in filez:
        if firstline is True:
            numberline = line.split()
            numbers = [int(n) for n in numberline]
            numbernodes.append(numbers)
            firstline = False;
        else:
            numberline = line.split(":")
            numbers = [int(n) for n in numberline]
            truenumbers.append(numbers)
    for x in range(numbernodes[0][0]):
        node = Node(x)
        graph.add_node(node)
        #print("Node" + str(x) + "added")
    for y in range(len(truenumbers)):
        edge = Edge(Node(truenumbers[y][0]), Node(truenumbers[y][1]), truenumbers[y][2])
        graph.add_edge(edge)
    return graph


class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)


class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        copy = self.adjacency_list[node_1.data]
        for x in range(len(copy)):
            if node_2.data is copy[x].to_node.data:
                return True
        return False

    def neighbors(self, node):
        neighbor = []
        if node.data in self.adjacency_list:
            copy = self.adjacency_list[node.data]
            for x in range(len(copy)):
                neighbor.append(copy[x].to_node)
            return neighbor
        else:
            return neighbor

    def add_node(self, node):
        if node.data in self.adjacency_list:
            return False
        else:
            self.adjacency_list[node.data] = []
            return True

    def remove_node(self, node):
        if node.data in self.adjacency_list:
            self.adjacency_list.pop(node.data)
            for key in self.adjacency_list:
                for x in range(len(self.adjacency_list[key])):
                    if self.adjacency_list[key][x].to_node.data is node.data:
                        del self.adjacency_list[key][x]
                        break
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge in self.adjacency_list[edge.from_node.data]:
            return False
        else:
            self.adjacency_list[edge.from_node.data].append(edge)
            return True

    def remove_edge(self, edge):
        if edge.from_node.data in self.adjacency_list:
            for x in range(len(self.adjacency_list[edge.from_node.data])):
                if edge in self.adjacency_list[edge.from_node.data]:
                    del self.adjacency_list[edge.from_node.data][x]
                    return True
            return False
        else:
            return False

    def returnEdge(self, node1, node2):
        edges = self.adjacency_list[node1.data]
        for edge in edges:
            if edge.to_node.data is node2.data:
                return edge

    def distance(self, node_1, node_2):
        pass

    def class_name(self):
        return "AL"


class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        index1 = 0
        index2 = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data is node_1.data:
                break
            else:
                index1 += 1
        for y in range(len(self.nodes)):
            if self.nodes[y].data is node_2.data:
                break
            else:
                index2 += 1

        if self.adjacency_matrix[index1][index2] >= 1:
            return True
        else:
            return False

    def neighbors(self, node):
        neighbors = []
        index = 0
        for x in self.nodes:
            if x.data is node.data:
                break
            else:
                index += 1
        index2 = 0
        for y in self.adjacency_matrix[index]:
            if y >= 1:
                neighbors.append(self.nodes[index2])
                index2 += 1
            else:
                index2 += 1
        return neighbors

    def add_node(self, node):
        length = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data is node.data:
                return False
        self.nodes.append(node)

        copy_matrix = list(self.adjacency_matrix)
        # print(copy_matrix)
        del self.adjacency_matrix[:]
        #print("Copy")
        #print(copy_matrix)
        length = len(copy_matrix) + 1
        # print(length)
        self.adjacency_matrix = [[0 for i in range(length)] for j in range(length)]
        #print("new AD")
        #print(self.adjacency_matrix)
        for x in range(length - 1):
            for y in range(length - 1):
                if x < len(copy_matrix):
                    if copy_matrix[x][y] >= 1:
                        self.adjacency_matrix[x][y] = copy_matrix[x][y]
                    else:
                        pass
                else:
                    # print(str(x))
                    self.adjacency_matrix[x][y] = 0

        for x in range(len(self.nodes)):
            if self.nodes[x].data is node.data:
                return True
            else:
                pass
        return False



    def remove_node(self, node):
        index = 0
        change = False
        for x in range(len(self.nodes)):
            #print(self.nodes[x].data)
            #print(node.data)
            if self.nodes[x].data == node.data:
                break
            else:
                index += 1
        if index is len(self.nodes):
            return False
        del self.adjacency_matrix[index]
        copy_mat = list(self.adjacency_matrix)
        del self.adjacency_matrix[:]
        self.adjacency_matrix = [[0 for i in range(len(copy_mat))] for j in range(len(copy_mat))]
        #print(len(self.adjacency_matrix))
        for r in range(len(self.adjacency_matrix)):
            for t in range(len(self.adjacency_matrix[r])):
                if t is index:
                    change = True
                if change is False:
                    self.adjacency_matrix[r][t] = copy_mat[r][t]
                else:
                    self.adjacency_matrix[r][t] = copy_mat[r][t + 1]
            change = False

        index = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data == node.data:
                del self.nodes[x]
                return True
            else:
                index += 1
        if index is len(self.nodes):
            return False

    def add_edge(self, edge):
        index1 = 0
        index2 = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data is edge.from_node.data:
                break
            else:
                index1 += 1
        for x in range(len(self.nodes)):
            if self.nodes[x].data is edge.to_node.data:
                break
            else:
                index2 += 1
        #print(self.adjacency_matrix)
        if len(self.adjacency_matrix) is 0:
            return False
        if self.adjacency_matrix[index1][index2] >= 1:
            return False
        else:
            self.adjacency_matrix[index1][index2] = edge.weight
            return True

    def remove_edge(self, edge):
        index1 = 0
        index2 = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data is edge.from_node.data:
                break
            else:
                index1 += 1
        for x in range(len(self.nodes)):
            if self.nodes[x].data is edge.to_node.data:
                break
            else:
                index2 += 1
        if len(self.adjacency_matrix) is 0:
            return False
        if self.adjacency_matrix[index1][index2] is 0:
            return False
        else:
            self.adjacency_matrix[index1][index2] = 0
            return True

    def returnEdge(self, node1, node2):
        index1 = 0
        index2 = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data is node1.data:
                break
            else:
                index1 += 1
        for y in range(len(self.nodes)):
            if self.nodes[y].data is node2.data:
                break
            else:
                index2 += 1
        edge = Edge(node1, node2, self.adjacency_matrix[index1][index2])
        #print edge
        return edge


    def __get_node_index(self, node):
        """helper method to find node index"""
        pass

    def distance(self, node_1, node_2):
        index1 = 0
        index2 = 0
        for x in range(len(self.nodes)):
            if self.nodes[x].data is node_1.data:
                break
            else:
                index1 += 1
        for y in range(len(self.nodes)):
            if self.nodes[y].data is node_2.data:
                break
            else:
                index2 += 1

        return self.adjacency_matrix[index1][index2]


    def class_name(self):
        return "AM"


class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for x in range(len(self.edges)):
            if node_1.data is self.edges[x].from_node.data:
                if self.edges[x].to_node.data is node_2.data:
                    return True
        return False

    def neighbors(self, node):
        neighbor = []
        for x in range(len(self.edges)):
            if node.data is self.edges[x].from_node.data:
                neighbor.append(self.edges[x].to_node)
        return neighbor

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            copy_edges = []
            for x in range(len(self.edges)):
                if node.data is self.edges[x].to_node.data:
                    copy_edges.append(self.edges[x])
            for x in range(len(copy_edges)):
                self.edges.remove(copy_edges[x])
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            return True

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False

    def returnEdge(self, node_1, node_2):
        edg = Edge(Node(0), Node(0), 1)
        for edge in self.edges:
            if edge.from_node.data is node_1.data and edge.to_node.data is node_2.data:
                return edge
        return edg

    def class_name(self):
        return "OO"


