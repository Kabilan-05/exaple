from collections import deque
def bfs(graph,start,visited=set()):
    print("1",type(graph))
    queue = deque([start])
    visited.add(start)
    print("2",type(visited))
    print("3",type(queue))
    while queue:
        node = queue.popleft()
        print("4",type(node))
        print(node,end= " ")
  
        for neighbour in graph[node]:
             print("5",type(graph))
             if neighbour not in visited:
                 print("6",type(neighbour))
                 print("7",type(visited))
                 print("8",type(queue))
                 visited.add(neighbour)
                 queue.append(neighbour)
path = {
    'A':['B','C'],
    'E':[],
    'B':['E'],
    'C':[]
    }
bfs(path,'A')
                        
