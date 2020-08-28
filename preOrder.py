#https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
class node(object):
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children

def preorder(root):
    preorderlist = []

    def preorder(node, resultList):
        preorderlist.append(node.val)
        if not node.children is None:
            for i in range(len(node.children)):
                preorder(node.children[i], preorderlist)

    preorder(root, preorderlist)
    return preorderlist

root = node(1,
    [
        node(3, [node(5), node(6)]),
        node(2),
        node(4)
    ])

print(preorder(root))