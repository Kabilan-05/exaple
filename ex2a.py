import heapq

# Node class to store coordinates and costs
class Node:
    def __init__(self, x, y, g=0, h=0, parent=None):
        self.x = x
        self.y = y
        self.g = g  # Cost from start to node
        self.h = h  # Heuristic cost from node to goal
        self.f = g + h  # Total cost
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

# Heuristic function (Manhattan Distance)
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# A* search algorithm
def a_star(grid, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, Node(start[0], start[1], 0, heuristic(start, goal)))

    while open_list:
        current = heapq.heappop(open_list)

        if (current.x, current.y) == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]  # Return reversed path

        closed_list.add((current.x, current.y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x, neighbor_y = current.x + dx, current.y + dy

            if (neighbor_x, neighbor_y) in closed_list or not is_walkable(grid, neighbor_x, neighbor_y):
                continue

            g = current.g + 1
            h = heuristic((neighbor_x, neighbor_y), goal)
            neighbor = Node(neighbor_x, neighbor_y, g, h, current)
            heapq.heappush(open_list, neighbor)

    return None  # No path found

# Helper function to check if a node is walkable
def is_walkable(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

# Example grid: 0 = walkable, 1 = obstacle
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)

print("Path:", path)
