class Edge:
    def __init__(self, vertex_from , vertex_to, distance):
        self._vertex_from = vertex_from
        self._vertex_to = vertex_to
        self._distance = distance

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, new_distance):
        self._distance = new_distance