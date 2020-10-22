#https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
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
                    

getApples = Solution()
print(getApples.minTime(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], [False,True,False,False,True,True]))