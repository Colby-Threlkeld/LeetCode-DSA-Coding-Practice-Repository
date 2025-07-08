from collections import deque

# creating Adjacency list graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS with graph
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        print("Queue:", list(queue))  # Visualize queue

        node = queue.popleft()
        if node not in visited:
            print("Visited:", node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

print("BFS:\n")
bfs(graph, 'A')

'''
Graph:
      A
     / \
    B   C
   / \   \
  D   E   F
       \
        F

Output:

BFS:

Queue: ['A']
Visited: A
Queue: ['B', 'C']
Visited: B
Queue: ['C', 'D', 'E']
Visited: C
Queue: ['D', 'E', 'F']
Visited: D
Queue: ['E', 'F']
Visited: E
Queue: ['F']
Visited: F

'''
