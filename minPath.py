##https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china

def minTime(n, edges, hasApple) -> int:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)
        secs = 0
        for child in adj[node]:
            secs += dfs(child)
        if secs > 0:
            return secs + 2
        return 2 if hasApple[node] else 0

    return max(dfs(0) - 2, 0)


##print(minTime(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], [False,True,False,False,True,True]))
print(minTime(3, [[0,2],[1,2]], [False,True,False]))


