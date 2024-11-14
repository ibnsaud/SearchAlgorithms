from queue import PriorityQueue
from typing import Union

from DataStructures.graph import AdjacencyVerticesGraph, ListEdgesGraph

class DijkstraSolver:

    def __init__(self, graph: Union[AdjacencyVerticesGraph, ListEdgesGraph]):
        self._graph = graph

    def solve_graph(self, start_vertex_id: int, stop_vertex_id: int):
        queue = PriorityQueue()
        updated_distances = {}
        updated_parents = {}
        explored = set()

        queue.put((0, start_vertex_id))
        updated_parents[start_vertex_id] = None

        while not queue.empty():
            cost, vertex = queue.get()
            explored.add(vertex)
            neighbors = self._graph.get_vertex_neighbors(vertex)
            for neighbor in neighbors:
                edge_to_neighbor = self._graph.get_vertex_cost(vertex, neighbor)

                if neighbor == start_vertex_id:
                    continue
                elif neighbor not in updated_distances:
                    updated_distances[neighbor] = cost + edge_to_neighbor
                    updated_parents[neighbor] = vertex
                elif updated_distances[neighbor] > updated_distances[vertex] + edge_to_neighbor:
                    updated_distances[neighbor] = updated_distances[vertex] + edge_to_neighbor
                    updated_parents[neighbor] = vertex

                if neighbor not in explored:
                    queue.put((updated_distances[neighbor], neighbor))

        lowest_cost = updated_distances[stop_vertex_id]

        lowest_cost_path = []
        vertex = stop_vertex_id
        while vertex is not None:
            lowest_cost_path.append(vertex)
            vertex = updated_parents[vertex]

        return lowest_cost, lowest_cost_path
