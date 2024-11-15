from DataStructures.graph import AdjacencyVerticesGraph, ListEdgesGraph
from SearchBFS import DijkstraSolver

def dijkstra_with_adjacency_graph():
    # create graph with adjacency matrix
    adjacency_graph = AdjacencyVerticesGraph(6)
    adjacency_graph.add_edge(0, 1, 5)
    adjacency_graph.add_edge(0, 2, 7)
    adjacency_graph.add_edge(1, 4, 5)
    adjacency_graph.add_edge(2, 1, 1)
    adjacency_graph.add_edge(2, 3, 3)
    adjacency_graph.add_edge(4, 3, 1)
    adjacency_graph.add_edge(3, 5, 1)
    adjacency_graph.add_edge(4, 5, 2)
    adjacency_graph.show_graph()

    # create dijkstra solver for graph
    dijkstra_solver = DijkstraSolver(adjacency_graph)
    cost, path = dijkstra_solver.solve_graph(0, 5)
    print(f'{cost=}, {path=}')

def dijkstra_with_list_edges_graph():
    # create graph with list of edges
    list_of_edges_graph = ListEdgesGraph()
    list_of_edges_graph.add_edge(0, 1, 5)
    list_of_edges_graph.add_edge(0, 2, 7)
    list_of_edges_graph.add_edge(1, 4, 5)
    list_of_edges_graph.add_edge(2, 1, 1)
    list_of_edges_graph.add_edge(2, 3, 3)
    list_of_edges_graph.add_edge(4, 3, 1)
    list_of_edges_graph.add_edge(3, 5, 1)
    list_of_edges_graph.add_edge(4, 5, 2)
    list_of_edges_graph.show_graph()

    # create dijkstra solver for graph
    dijkstra_solver = DijkstraSolver(list_of_edges_graph)
    cost, path = dijkstra_solver.solve_graph(0, 5)
    print(f'{cost=}, {path=}')

def main():
    dijkstra_with_adjacency_graph()
    dijkstra_with_list_edges_graph()

if __name__ == '__main__':
    main()