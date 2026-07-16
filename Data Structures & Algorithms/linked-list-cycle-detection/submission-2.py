# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        temp = head
        repeated = 0
        while temp:
            if(temp.val in seen):
                repeated += 1
            seen.add(temp.val)
            temp = temp.next
            if repeated > 3:
                return True
        return False