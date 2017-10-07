"""
Searches module defines all different search algorithms
"""
import Queue

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    q = Queue.Queue()
    q.put(initial_node)
    nodeParent = {}
    nodeParent[initial_node] = None
    endNode = None

    while not q.empty():
        current = q.get()

        if current.data is dest_node.data:
            endNode = current
            break

        for next in graph.neighbors(current):
            if next not in nodeParent:
                q.put(next)
                nodeParent[next] = current

    finalList = []
    if graph.class_name() is "AL":
        while nodeParent[endNode] is not None:
            for x in graph.adjacency_list[nodeParent[endNode].data]:
                if x.from_node.data is nodeParent[endNode].data and x.to_node.data is endNode.data:
                    finalList.append(x)
                    break
            endNode = nodeParent[endNode]
        finalList.reverse()
        return finalList
    elif graph.class_name() is "AM":
        while nodeParent[endNode] is not None:
            edge = graph.edgeReturn()
            edge.from_node = nodeParent[endNode]
            edge.to_node = endNode
            edge.weight = graph.distance(nodeParent[endNode], endNode)
            finalList.append(edge)
            endNode = nodeParent[endNode]
        finalList.reverse()
        return finalList
    else:
        while nodeParent[endNode] is not None:
            finalList.append(graph.returnEdge(nodeParent[endNode], endNode))
            endNode = nodeParent[endNode]
        finalList.reverse()
        return finalList



def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
