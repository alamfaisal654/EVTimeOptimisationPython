class Node:
    def __init__(self, _node_id, _node_lat, _node_long):
        self.node_id = _node_id
        self.node_lat = _node_lat
        self.node_long = _node_long
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)
        
