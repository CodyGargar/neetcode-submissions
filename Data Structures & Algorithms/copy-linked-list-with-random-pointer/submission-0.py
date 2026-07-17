"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        ranmap = {}

        curr = head
        while(curr):
            ranmap[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while(curr):
            temp = ranmap[curr]
            if curr.next:
                temp.next = ranmap[curr.next]
            if curr.random:
                temp.random = ranmap[curr.random]
            curr = curr.next

        return ranmap[head]
