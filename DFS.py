class DFS:
    def __init__(self, n):
        self.nodeNumber = n
        self.adj = [[] for _ in range(n)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def DFSUntil(self, n, visited):
        visited[n] = True
        print(n)

        for next in self.adj[n]:
            if not visited[next]:
                self.DFSUntil(next, visited)

    def dfs(self, n):
        visited = [False] * self.nodeNumber

        self.DFSUntil(n, visited)

g = DFS(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(1,3)
g.addEdge(0,4)
g.addEdge(3,4)
g.addEdge(4,5)

g.dfs(2)
