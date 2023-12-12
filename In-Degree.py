def find_in_degree(adj_list, n):
  in_degree = [0] * n

  for adj_vertices in adj_list:
    for vertex in adj_vertices:
      # Every vertex that has an incoming edge from vertex i
      in_degree[vertex] += 1

  for k in range(n):
    print(f"Vertex {k} has in-degree: {in_degree[k]}")


if __name__ == "__main__":
  # Adjacency list representation of the graph
  adjacency = [
    [3, 4],  # Vertices 3 and 4 have an incoming edge from vertex 0
    [3, 2],  # Vertex 3 and 2 has an incoming edge from vertex 1
    [],  # no incoming edge from vertex 2
    [2, 4],  # Vertices 2 and 4 have an incoming edge from vertex 3
    [2, 3],  # Vertices 2 and 3 have an incoming edge from vertex 4
    [1, 4, 6],  # Vertices 1, 4, and 6 have an incoming edge from vertex 5
    [5]  # Vertex 5 has an incoming edge from vertex 6
  ]

  n = len(adjacency)
  find_in_degree(adjacency, n)

"""
public class Solution {
    public int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;

        int count_of_3s = n / 3;
        int remainder = n % 3;

        if (remainder == 0) {
            return (int) Math.pow(3, count_of_3s);
        } else if (remainder == 1) {
            return (int) Math.pow(3, count_of_3s - 1) * 4;
        } else {
            return (int) Math.pow(3, count_of_3s) * 2;
        }
    }
}
"""