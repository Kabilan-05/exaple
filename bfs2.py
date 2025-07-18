from collections import deque

def bfs(grid, start, goal):

    rows, cols = len(grid), len(grid[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    queue = deque([(start, 0)])  # (position, steps)

    visited = set([start])

    while queue:

        (x, y), steps = queue.popleft()

        if (x, y) == goal:

            return steps  # Shortest path found

        for dx, dy in directions:

            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:

                queue.append(((nx, ny), steps + 1))

                visited.add((nx, ny))

    return -1  # No path found

# Example Grid (0 = Open, 1 = Obstacle)

grid = [

    [0, 1, 0, 0, 0],

    [0, 1, 0, 1, 0],

    [0, 0, 0, 1, 0],

    [1, 1, 1, 1, 0],

    [0, 0, 0, 0, 0]

]

start = (0, 0)  # Start at top-left corner

goal = (4, 4)   # Goal at bottom-right corner

print("Shortest Path Length using BFS:", bfs(grid, start, goal))
