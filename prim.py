import heapq

def prim(graph):
    min_spanning_tree = []
    visited = set()
    start_node = next(iter(graph))
    visited.add(start_node)
    edges = [(cost, start_node, to) for to, cost in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            min_spanning_tree.append((frm, to, cost))
            for next_to, next_cost in graph[to]:
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

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
print("\nPrim's Minimal Spanning Tree:")
print(prim(graph))
