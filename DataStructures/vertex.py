class Vertex:
    def __init__(self, vertex_id: int, parent: 'Vertex' = None, cost: int = 0):
        self._vertex_id = vertex_id
        self._neighbor_edges = {}
        self._cost = cost
        self._parent = parent

    @property
    def vertex_id(self):
        return self._vertex_id

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_distance):
        self._cost = new_distance

    @property
    def neighbors(self):
        return self._neighbor_edges

    def add_neighbor(self, vertex_id, neighbor_vertex: 'Vertex'):
        self._neighbor_edges[vertex_id] = neighbor_vertex

    def get_neighbor(self, vertex_id):
        return self._neighbor_edges[vertex_id]