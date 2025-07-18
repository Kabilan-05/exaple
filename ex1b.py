# Recursive implementation of DFS
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# Call the function
visited = set()
dfs_recursive(graph, 'A', visited)
