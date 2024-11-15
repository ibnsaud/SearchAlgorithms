from queue import PriorityQueue
from typing import Union

from DataStructures.graph import AdjacencyVerticesGraph, ListEdgesGraph

class DijkstraSolver:

    def __init__(self, graph: Union[AdjacencyVerticesGraph, ListEdgesGraph]):
        self._graph = graph

    def solve_graph(self, start_vertex_id: int, stop_vertex_id: int):
        if start_vertex_id not in self._graph.get_all_vertices():
            raise ValueError("Start vertex does not exist.")
        if stop_vertex_id not in self._graph.get_all_vertices():
            raise ValueError("Stop vertex does not exist.")
        queue = PriorityQueue()
        updated_distances = {vertex_id: float('inf') for vertex_id in self._graph.get_all_vertices()}
        updated_parents = dict()

        updated_parents[start_vertex_id] = None
        updated_distances[start_vertex_id] = 0
        queue.put((0, start_vertex_id))

        while not queue.empty():
            cost, vertex = queue.get()
            if vertex == stop_vertex_id:
                break
            neighbors = self._graph.get_vertex_neighbors(vertex)
            for neighbor in neighbors:
                edge_to_neighbor = self._graph.get_vertex_cost(vertex, neighbor)
                if updated_distances[neighbor] > cost + edge_to_neighbor:
                    updated_distances[neighbor] = cost + edge_to_neighbor
                    updated_parents[neighbor] = vertex
                    queue.put((updated_distances[neighbor], neighbor))
        lowest_cost = updated_distances[stop_vertex_id]

        lowest_cost_path = []
        vertex = stop_vertex_id
        while vertex is not None:
            lowest_cost_path.append(vertex)
            vertex = updated_parents[vertex]
        lowest_cost_path.reverse()
        return lowest_cost, lowest_cost_path
