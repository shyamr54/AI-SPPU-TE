import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

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
start_node = input("Enter the start node: ")
distances = dijkstra(graph, start_node)
print("\nShortest distances from", start_node + ":")
for node, distance in distances.items():
    print("To", node + ":", distance)

"""Enter the number of nodes: 4
Enter node name: A
Enter the number of edges for node A: 2
Enter neighbor node and cost separated by space: B 2
Enter neighbor node and cost separated by space: C 3
Enter node name: B
Enter the number of edges for node B: 3
Enter neighbor node and cost separated by space: A 2
Enter neighbor node and cost separated by space: C 1
Enter neighbor node and cost separated by space: D 1
Enter node name: C
Enter the number of edges for node C: 3
Enter neighbor node and cost separated by space: A 3
Enter neighbor node and cost separated by space: B 1
Enter neighbor node and cost separated by space: D 2
Enter node name: D
Enter the number of edges for node D: 2
Enter neighbor node and cost separated by space: B 1
Enter neighbor node and cost separated by space: C 2
Enter the start node: A
"""