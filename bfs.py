from collections import deque

def bfs(graph, start):

    visited = set()  # To track visited nodes

    queue = deque([start])  # Initialize a queue with the starting node

    visited.add(start)  # Mark the starting node as visited

    while queue:

        node = queue.popleft()  # Dequeue a node from the front of the queue

        print(node, end=" ")  # Process the node (e.g., print its value)

        # Enqueue all unvisited neighbors

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)  # Mark the neighbor as visited

                queue.append(neighbor)  # Add the neighbor to the queue

# Example graph represented as an adjacency list

graph = {

    'A': ['B', 'C'],

    'B': ['D', 'E'],

    'C': ['F'],

    'D': [],

    'E': ['F'],

    'F': []

}

# Perform BFS starting from node 'A'

bfs(graph, 'B')  # Output: A B C D E F
