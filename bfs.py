from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
if __name__ == "__main__":
    g = Graph()
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("BFS Traversal starting from vertex 2:")
    g.bfs(2)