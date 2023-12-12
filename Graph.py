class Graph:

  def __init__(self):
    self.graph = {}

  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = []

  def add_edge(self, vertex1, vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      self.graph[vertex1].append(vertex2)
      self.graph[vertex2].append(vertex1)

  def remove_edge(self, vertex1, vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      self.graph[vertex1].remove(vertex2)
      self.graph[vertex2].remove(vertex1)

  def remove_vertex(self, vertex):
    if vertex in self.graph:
      del self.graph[vertex]
      for vertices in self.graph.values():
        if vertex in vertices:
          vertices.remove(vertex)

  def get_neighbors(self, vertex):
    if vertex in self.graph:
      return self.graph[vertex]
    else:
      return []

  def __str__(self):
    return str(self.graph)


# Example usage:
graph = Graph()

# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')

# Remove an edge
graph.remove_edge('B', 'C')

# Remove a vertex
graph.remove_vertex('D')

# Get neighbors of a vertex
print(graph.get_neighbors('A'))

# Print the graph
print(graph)
