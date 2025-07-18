from collections import deque

def bfs(graph,visited,start):

    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        #if node == goal:
        print(node,end=" ")
            #return node
        for neighbour in graph[node]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(neighbour)
        #return False

def dfs(graph,node,visited=set()):

    if node not in visited:

        print(node,end=" ")

        visited.add(node)

        for neighbour in graph[node]:

            #if neighbour not in visited:

            dfs(graph,neighbour,visited)

graph = { 'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}

visited = set()

start = 'A'

bfs(graph,visited,start)

#dfs(graph,start,visited)

