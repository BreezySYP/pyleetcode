#https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildTree(self, values):
        root = TreeNode()
        root.val = values[0]

        for i in range(1, len(values)):
            self.insert(root, values[i])

        return root

    def insert(self, node, value):
        if not node:
            node = TreeNode()
            node.val = value
            return

        if node.val > value:
            self.insert(node.left, value)
        elif node.val < value:
            self.insert(node.right, value)
                


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

