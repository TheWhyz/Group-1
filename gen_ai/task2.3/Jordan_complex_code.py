import heapq

def dijkstra(graph, start, end):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break  # Found the shortest path

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct shortest path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, distances[end]

# Example Graph (Adjacency List Representation)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 8},
    'E': {'D': 8}
}

# Find shortest path from 'A' to 'E'
path, distance = dijkstra(graph, 'A', 'E')
print(f"Shortest Path: {path}, Distance: {distance}")


#make complex code easier to understand 

import heapq
from collections import defaultdict, deque

def dijkstra(graph, start, end):
    """Finds the shortest path and distance using Dijkstra's Algorithm."""
    
    if start not in graph or end not in graph:
        return None, float('inf')  # Handle missing nodes
    
    priority_queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break  # Stop when reaching the destination

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:  # Found a shorter path
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return reconstruct_path(previous_nodes, start, end), distances[end]

def reconstruct_path(previous_nodes, start, end):
    """Reconstructs the shortest path from end to start."""
    path = deque()
    current = end

    while current in previous_nodes:
        path.appendleft(current)
        current = previous_nodes[current]

    if path:
        path.appendleft(start)  # Add the starting node
    
    return list(path) if path else None  # Return None if no path found

# Example Graph (Adjacency List Representation)
graph = defaultdict(dict, {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 8},
    'E': {'D': 8}
})

# Find shortest path from 'A' to 'E'
path, distance = dijkstra(graph, 'A', 'E')

if path:
    print(f"Shortest Path: {path}, Distance: {distance}")
else:
    print("No valid path found.")
