from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph.graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Construct a simple graph
#   0 -- 1
#   |    |
#   3 -- 2
graph = Graph()
graph.add_edge(0, [1, 3])
graph.add_edge(1, [0, 2])
graph.add_edge(2, [1, 3])
graph.add_edge(3, [0, 2])

# Perform BFS starting from vertex 0
print("BFS:")
bfs(graph, 0)
print()

# Perform DFS starting from vertex 0
print("DFS:")
dfs(graph, 0)
print()
