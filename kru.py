class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(graph):
    min_spanning_tree = []
    edges = [(cost, frm, to) for frm in graph for to, cost in graph[frm]]
    edges.sort()

    disjoint_set = DisjointSet(len(graph))

    for cost, frm, to in edges:
        if disjoint_set.find(frm) != disjoint_set.find(to):
            min_spanning_tree.append((frm, to, cost))
            disjoint_set.union(frm, to)

    return min_spanning_tree

def get_graph_from_input():
    graph = {}
    nodes = int(input("Enter the number of nodes: "))
    for _ in range(nodes):
        node = input("Enter node name: ")
        graph[node] = []
        edges = int(input(f"Enter the number of edges for node {node}: "))
        for _ in range(edges):
            neighbor, cost = input("Enter neighbor node and cost separated by space: ").split()
            graph[node].append((neighbor, int(cost)))
    return graph

# Example usage:
print("Enter the graph details:")
graph = get_graph_from_input()
print("\nKruskal's Minimal Spanning Tree:")
print(kruskal(graph))
