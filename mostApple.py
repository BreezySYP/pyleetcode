class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        stack = []
        edgesRemovalList = edges.copy()
        pathCount = 0
        
        while len(edges) > 0 or len(stack) > 0:
            edges = edgesRemovalList.copy()

            for edge in edges:
                if len(stack) == 0 or stack[-1][1] == edge[0]:
                    stack.append(edge)
                    edgesRemovalList[edges.index(edge)] = True
            
            popEdge = stack.pop()
            if hasApple[popEdge[1]]:
                pathCount += 2
                if len(stack) > 0:
                    hasApple[stack[-1][1]] = True
        
        return pathCount
                    

getApples = Solution()
print(getApples.minTime(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], [False,True,False,False,True,True]))