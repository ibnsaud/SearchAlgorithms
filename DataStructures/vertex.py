class Vertex:
    def __init__(self):
        self._neighbor_edges = {}
        self._shortest_distance = None
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def shortest_distance(self):
        return self._shortest_distance

    @shortest_distance.setter
    def shortest_distance(self, new_distance):
        self._shortest_distance = new_distance

    def add_neighbor(self, vertex_id, neighbor_vertex: 'Vertex'):
        self._neighbor_edges[vertex_id] = neighbor_vertex

    def get_neighbor(self, vertex_id):
        return self._neighbor_edges[vertex_id]