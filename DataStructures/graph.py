class AdjacencyVerticesGraph:
    def __init__(self, max_vertices, is_directed=False):
        self._max_vertices = max_vertices
        self._is_directed = is_directed
        self._count = 0
        self._graph = [[0]*self._max_vertices for _ in range(self._max_vertices)]

    def add_edge(self, vertex_id_from: int, vertex_id_to: int, weight: int = 1):
        if (vertex_id_from < 0) or (vertex_id_from >= self._max_vertices):
            raise IndexError(f'Index {vertex_id_from=} out of range.')
        if (vertex_id_to < 0) or (vertex_id_to >= self._max_vertices):
            raise IndexError(f'Index {vertex_id_to=} out of range.')
        self._graph[vertex_id_from][vertex_id_to] = weight
        if not self._is_directed:
            self._graph[vertex_id_to][vertex_id_from] = weight

    def get_vertex_cost(self, vertex_id_from, vertex_id_to):
        return self._graph[vertex_id_from][vertex_id_to]

    def get_vertex_neighbors(self, vertex_id: int):
        return [neighbor_id for neighbor_id in range(self._max_vertices) if self._graph[vertex_id][neighbor_id] != 0]

    def show_graph(self):
        for row in self._graph:
            print(*row)