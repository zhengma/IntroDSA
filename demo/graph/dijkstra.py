from graph import Graph

class Dijkstra:
    
    def __init__(self, network: Graph, start):
        self.MAX_DIST = 65535
        self.network = network
        try:
            if start in network.vertices:
                self.start = start
            else:
                raise ValueError(start)
        except ValueError as ve:
            print(f'\'{start}\' is not in the graph!')
        self.todo = self.network.vertices
        self.min_paths = {vertex: ['', self.MAX_DIST] for vertex in self.todo}
        self.min_paths[start] = [f'{start}', 0]
    
    def next_node(self):
        next = self.todo[0]
        for vertex in self.todo:
            if self.min_paths[vertex][1] < self.min_paths[next][1]:
                next = vertex
        return self.todo.index(next)
    
    def solve(self):
        while self.todo:
            current = self.todo.pop(self.next_node())
            baseline = self.min_paths[current]
            for neighbour in self.network.edges[current]:
                node = neighbour[0]
                edge = neighbour[1]
                if baseline[1] + edge < self.min_paths[node][1]:
                    self.min_paths[node][0] = f'{baseline[0]}-{node}'
                    self.min_paths[node][1] = baseline[1] + edge

if __name__ == "__main__":
    test_g = Graph(list('ABCDEFG'))
    print(test_g.edges)
    test_g.add_edge([('A', 'B', 5), ('A', 'C', 6), ('B', 'D', 4), 
                     ('B', 'E', 6), ('C', 'E', 7), ('C', 'F', 6),
                     ('D', 'E', 3), ('D', 'G', 12), ('E', 'F', 5),
                     ('E', 'G', 6), ('F', 'G', 8)])
    solver = Dijkstra(test_g, 'A')
    # print(solver.min_paths)
    solver.solve()
    print(solver.min_paths)