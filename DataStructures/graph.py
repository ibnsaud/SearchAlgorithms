class AdjacencyVerticesGraph:
    def __init__(self, max_vertices, is_directed=False):
        self._max_vertices = max_vertices
        self._is_directed = is_directed
        self._count = 0
        self._vertices = [[0]*self._max_vertices for _ in range(self._max_vertices)]

    def add_edge(self, vertex_id_from: int, vertex_id_to: int, weight: int = 1):
        if (vertex_id_from < 0) or (vertex_id_from >= self._max_vertices):
            raise IndexError(f'Index {vertex_id_from=} out of range.')
        if (vertex_id_to < 0) or (vertex_id_to >= self._max_vertices):
            raise IndexError(f'Index {vertex_id_to=} out of range.')
        self._vertices[vertex_id_from][vertex_id_to] = weight
        if not self._is_directed:
            self._vertices[vertex_id_to][vertex_id_from] = weight

    def get_vertex_cost(self, vertex_id_from, vertex_id_to):
        return self._vertices[vertex_id_from][vertex_id_to]

    def get_vertex_neighbors(self, vertex_id: int):
        return [neighbor_id for neighbor_id in range(self._max_vertices) if self._vertices[vertex_id][neighbor_id] != 0]

    def show_graph(self):
        for row in self._vertices:
            print(*row)

class ListEdgesGraph:
    def __init__(self, is_directed=False):
        self._edges = []
        self._is_directed = is_directed

    def add_edge(self, vertex_id_from: int, vertex_id_to: int, weight: int = 1):
        self._edges.append((vertex_id_from, vertex_id_to, weight))

    def get_vertex_cost(self, vertex_id_from, vertex_id_to):
        cost = None
        for vertex_from, vertex_to, weight in self._edges:
            if (vertex_from == vertex_id_from) and (vertex_to == vertex_id_to):
                cost = weight
            elif (vertex_id_from == vertex_to) and (vertex_id_to == vertex_from) and not (self._is_directed):
                cost = weight
        if cost is None:
            raise NameError(f'Edge from {vertex_id_from} to {vertex_id_to} does not exist.')
        return cost

    def get_vertex_neighbors(self, vertex_id: int):
        neighbors = []
        for vertex_from, vertex_to, _ in self._edges:
            if vertex_from == vertex_id:
                neighbors.append(vertex_to)
            if not self._is_directed and vertex_to == vertex_id:
                neighbors.append(vertex_from)
        return neighbors

    def show_graph(self):
        print(*self._edges, sep='\n')