#https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, root, newNode):
        que = deque()
        que.append(self)
        while len(que) > 0:
            node = que[0]
            que.popleft()

            if node.left == None:
                node.left = newNode
                return
            if node.right == None:
                node.right = newNode
                return

            que.append(node.left)
            que.append(node.right)

    def printTree(self):
        que = deque()
        que.append(self)
        message = ''
        while len(que) > 0:
            node = que[0]
            message += str(node.val) + ' '
            que.popleft()
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)

        print(message)
        

def arrayToTree(values):
    root = TreeNode(values[0])
    for i in range(1, len(values)):
        newnode = TreeNode(values[i])
        root.insert(root, newnode)

    return root

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return root.val

        resultlist = []
        self.leafstring(root.left, str(root.val), resultlist)
        self.leafstring(root.right, str(root.val), resultlist)

        return sum([int(binary, 2) for binary in resultlist])
        

    def leafstring(self, node, code, resultlist):
        if node == None:
            return
        binaryCode = code + str(node.val)

        if node.left == None and node.right == None:
            resultlist.append(binaryCode)

        self.leafstring(node.left, binaryCode, resultlist)
        self.leafstring(node.right, binaryCode, resultlist)

sol = Solution()
root = arrayToTree([1,0,1,0,1,0,1])
root.printTree()
print(sol.sumRootToLeaf(root))