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
    nodeParent = {}
    nodes = []
    isFound = [0]
    nodeParent[initial_node] = None
    nodes.append(initial_node)

    def DFS(node, parentNode, nodes, isFound):
        if isFound is 1:
            return
        else:
            if node not in nodeParent:
                nodeParent[node] = parentNode
            if node.data is dest_node.data:
                del nodes[:]
                nodes.append(node)
                isFound[0] = 1
            elif len(graph.neighbors(node)) is 0:
                nodes.pop()
            else:
                for next in graph.neighbors(node):
                    nodes.append(next)
                    DFS(next, node, nodes, isFound)

    DFS(initial_node, None, nodes, isFound)

    end = nodes[0]

    finalList = []

    if graph.class_name() is "AL":
        while nodeParent[end] is not None:
            for x in graph.adjacency_list[nodeParent[end].data]:
                if x.from_node.data is nodeParent[end].data and x.to_node.data is end.data:
                    finalList.append(x)
                    break
            end = nodeParent[end]
        finalList.reverse()
        return finalList
    elif graph.class_name() is "AM":
        while nodeParent[end] is not None:
            edge = graph.edgeReturn()
            edge.from_node = nodeParent[end]
            edge.to_node = end
            edge.weight = graph.distance(nodeParent[end], end)
            finalList.append(edge)
            end = nodeParent[end]
        finalList.reverse()
        return finalList
    else:
        while nodeParent[end] is not None:
            finalList.append(graph.returnEdge(nodeParent[end], end))
            end = nodeParent[end]
        finalList.reverse()
        return finalList

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    distance = {}
    nodeParent = {}
    distance[initial_node] = 0
    nodeParent[initial_node] = None

    prio = Queue.PriorityQueue()
    prio.put((distance[initial_node], initial_node))

    fina = None

    while not prio.empty():
        node = prio.get()[1]

        if node.data is dest_node.data:
            fina = node
            break
        for nex in graph.neighbors(node):
            if nex not in nodeParent:
                nodeParent[nex] = node
            if nex not in distance:
                distance[nex] = 999
            alt = distance[node] + graph.returnEdge(node, nex).weight
            if alt < distance[nex]:
                distance[nex] = alt
                nodeParent[nex] = node
                prio.put((distance[nex], nex))

    finalList = []
    while nodeParent[fina] is not None:
        finalList.append(graph.returnEdge(nodeParent[fina], fina))
        fina = nodeParent[fina]
    finalList.reverse()
    return finalList

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
