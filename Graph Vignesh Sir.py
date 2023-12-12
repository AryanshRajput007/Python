class Graph:
    class Edge:
        def __init__(self):
            self.src = 0
            self.dest = 0
    
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.edge = [self.Edge() for _ in range(edges)]
    
    @staticmethod
    def main(args):
        noVertices = 5
        noEdges = 7
        g = Graph(noVertices, noEdges)
        g.edge[0].src = 1
        g.edge[0].dest = 2
        g.edge[1].src = 1
        g.edge[1].dest = 3
        g.edge[2].src = 1
        g.edge[2].dest = 4
        g.edge[3].src = 2
        g.edge[3].dest = 4
        g.edge[4].src = 2
        g.edge[4].dest = 3
        g.edge[5].src = 3
        g.edge[5].dest = 4
        g.edge[6].src = 3
        g.edge[6].dest = 5
      