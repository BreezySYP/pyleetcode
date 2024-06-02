#https://leetcode-cn.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        tolist = [head.val]
        current = head

        while current.next is not None:
            current = current.next
            tolist.append(current.val)
        
        return tolist == tolist[::-1]


def buildList(vals):
    root = ListNode(vals[0])
    current = root
    for i in range(1, len(vals)):
        current.next = ListNode(vals[i])
        current = current.next

    return root

sol = Solution()
root = buildList([1,2,3,3,2,2,3,3,2,1])
print(sol.isPalindrome(root))

    
        