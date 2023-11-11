class Graph:
    def __init__(self, vertices: list, directed: bool = False):
        self.vertices = vertices
        self.edges = {vertex: set() for vertex in vertices}
        self.directed = directed
    
    def add_edge(self, edges: list[tuple]):
        for edge in edges:
            try:
                if edge[0] not in self.vertices:
                    raise ValueError(edge[0])
                if edge[1] not in self.vertices:
                    raise ValueError(edge[1])
                self.edges[edge[0]].add((edge[1], edge[2]))
                if not self.directed:
                    self.edges[edge[1]].add((edge[0], edge[2]))
            except IndexError:
                print('Each edge has to be a 3-tuple!')
            except ValueError as ve:
                print(f'Node \'{ve}\' nonexist!')

    def to_adj_matrix(self) -> list[list]:
        matrix = t = [[0]*len(self.vertices) for v in self.vertices]
        for from_node, neighbours in self.edges.items():
            idx_from = self.vertices.index(from_node)
            for neighbor in neighbours:
                idx_to = self.vertices.index(neighbor[0])
                matrix[idx_from][idx_to] = neighbor[1]
        return matrix

if __name__ == "__main__":
    test_g = Graph(list('ABC'))
    print(test_g.edges)
    test_g.add_edge([('A', 'B', 5), ('A', 'C', 6)])
    print(test_g.edges)
    print(test_g.to_adj_matrix())
    # print(test_g.vertices[1])