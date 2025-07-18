# Recursive DFS function
def dfs_recursive(tree, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    visited.add(node)    # Mark the node as visited
    print(node,end="")          # Print the current node (for illustration)
    for child in tree[node]:  # Recursively visit children
        if child not in visited:
            dfs_recursive(tree, child, visited)
    return visited

# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# Run DFS starting from node 'A'

print("DFS traversal is:",dfs_recursive(tree, 'A'))
