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
    def __init__(self, from_node, to_node, weight, from_name, to_name):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
        self.from_name = from_name
        self.to_name = to_name
    def __str__(self):
        return 'Edge(from {}, to {}, weight {}, fromName {}, toName {})'.format(self.from_node, self.to_node, self.weight, self.from_name, self.to_name)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {}, fromName {}, toName {})'.format(self.from_node, self.to_node, self.weight, self.from_name, self.to_name)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight and self.from_name == other_node.from_name and self.to_name == other_node.to_name
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight, self.from_name, self.to_name))

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
    '''
    graph = ObjectOriented()
    q = Queue.Queue()
    q.put(empty_room)
    nodeParent = {}
    nodeParent[empty_room['id']] = None
    endNode = None

    #print(empty_room['location']['name'])

    while not q.empty():
        current = q.get()

        if current['location']['name'] == "Dark Room" and current['id'] == "f1f131f647621a4be7c71292e79613f9":
            endNode = current['id']
            break

        for x in current['neighbors']:
            new_room = get_state(x['id'])
            if new_room['id'] not in nodeParent:
                nodeParent[new_room['id']] = current['id']
                edge = Edge(current['id'], x['id'], transition_state(current['id'], x['id'])['event']['effect'], current['location']['name'], x['location']['name'])
                graph.edges.append(edge)
                q.put(new_room)

    finalList = []

    while nodeParent[endNode] is not None:
        finalList.append(graph.returnEdge(nodeParent[endNode], endNode))
        endNode = nodeParent[endNode]
    finalList.reverse()

    hp = 0
    print("BFS Path:")
    for x in finalList:
        print(x.from_name + "(" + str(x.from_node) + ") : " + x.to_name + "(" + str(x.to_node) + "): " + str(x.weight))
        hp += x.weight
    print("Total HP: " + str(hp))

    print(" ")
    '''
    graph2 = ObjectOriented()

    distance = {}
    nodeP = {}
    numPrio = {}
    distance[empty_room['id']] = 0
    nodeP[empty_room['id']] = None
    numPrio[empty_room['id']] = 1
    visited = []
    finaDist = -999

    q2 = Queue.PriorityQueue()
    q2.put((numPrio[empty_room['id']], empty_room))

    fina = "f1f131f647621a4be7c71292e79613f9"
    finalL = []

    while not q2.empty():
        cur = q2.get()[1]

        if cur['location']['name'] == "Dark Room" and cur['id'] == "f1f131f647621a4be7c71292e79613f9":
            dist = 0
            testL = []
            while nodeP[fina] is not None:
                dist += graph2.returnEdge(nodeP[fina], fina).weight
                testL.append(graph2.returnEdge(nodeP[fina], fina))
                fina = nodeP[fina]
            testL.reverse()

            if dist > finaDist:
                finaDist = dist
                finalL = testL
            print(dist)
            fina = cur['id']
            continue

        if cur['id'] in visited:
            continue

        for x in cur['neighbors']:
            new_r = get_state(x['id'])
            if new_r['id'] in visited:
                continue
            if new_r['id'] not in numPrio:
                numPrio[new_r['id']] = 1.0
            # if new_r['id'] not in nodeP:
            # nodeP[new_r['id']] = cur['id']
            if new_r['id'] not in distance:
                distance[new_r['id']] = -999
            edge = Edge(cur['id'], new_r['id'], transition_state(cur['id'], new_r['id'])['event']['effect'],
                        cur['location']['name'], new_r['location']['name'])

            alt = distance[cur['id']] + edge.weight

            if alt >= distance[new_r['id']]:
                graph2.edges.append(edge)
                distance[new_r['id']] = alt
                nodeP[new_r['id']] = cur['id']
                numPrio[new_r['id']] /= 2
                q2.put((numPrio[new_r['id']], new_r))
        visited.append(cur['id'])

    hp = 0

    print(len(visited))
    print("DFS Path:")
    for x in finalL:
        print(x.from_name + "(" + str(x.from_node) + ") : " + x.to_name + "(" + str(x.to_node) + "): " + str(x.weight))
        hp += x.weight
    print("Total HP: " + str(hp))

    #print(empty_room['neighbors'])
    #print(empty_room['id'])
    #print(empty_room['neighbors'][0]['location']['name'])
    #print()
    #print(transition_state(empty_room['id'], empty_room['neighbors'][3]['id']))