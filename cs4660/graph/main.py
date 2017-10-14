"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import Queue

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

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

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def neighbors(self, node):
        neighbor = []
        for edge in self.edges:
            if node['id'] is edge.from_node['id']:
                neighbor.append(edge.to_node)
        return neighbor

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            return True

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def returnEdge(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return edge

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response


if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')

    graph = ObjectOriented()
    q = Queue.Queue()
    q.put(empty_room)
    nodeParent = {}
    nodeParent[empty_room['id']] = None
    endNode = None

    #print(empty_room['location']['name'])

    while not q.empty():
        current = q.get()

        if current['location']['name'] == "Dark Room":
            endNode = current['id']
            break

        for x in current['neighbors']:
            new_room = get_state(x['id'])
            if new_room['id'] not in nodeParent:
                nodeParent[new_room['id']] = current['id']
                edge = Edge(current['id'], x['id'], transition_state(current['id'], x['id'])['event']['effect'])
                graph.edges.append(edge)
                q.put(new_room)
            if new_room['location']['name'] == "Dark Room":
                endNode = current['id']
                break

    finalList = []

    while nodeParent[endNode] is not None:
        finalList.append(graph.returnEdge(nodeParent[endNode], endNode))
        endNode = nodeParent[endNode]
    finalList.reverse()
    print("BFS")
    print("Path to get to Dark Room")
    for x in finalList:
        print(x)

    print()
    print("DFS not implemented")


    #print(empty_room['neighbors'])
    #print(empty_room['id'])
    #print(empty_room['neighbors'][0]['location']['name'])
    #print()
    #print(transition_state(empty_room['id'], empty_room['neighbors'][3]['id']))