from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            vertex = queue.pop(0)
            print(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Take user input for graph edges
def take_input():
    edges = []
    while True:
        edge = input("Enter an edge (or 'done' to finish): ")
        if edge.lower() == 'done':
            break
        u, v = map(int, edge.split())
        edges.append((u, v))
    return edges

# Example usage:
g = Graph()

# Take input for graph edges
edges = take_input()
for edge in edges:
    g.add_edge(*edge)

# Take input for starting vertex
start_vertex = int(input("Enter the starting vertex for traversal: "))

print("\nDFS traversal:")
g.dfs(start_vertex)

print("\nBFS traversal:")
g.bfs(start_vertex)

"""Enter an edge (or 'done' to finish): 0 1
Enter an edge (or 'done' to finish): 0 2
Enter an edge (or 'done' to finish): 1 2
Enter an edge (or 'done' to finish): 2 3
Enter an edge (or 'done' to finish): 3 4
Enter an edge (or 'done' to finish): done
Enter the starting vertex for traversal: 0
"""