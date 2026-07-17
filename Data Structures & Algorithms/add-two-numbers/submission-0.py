# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        ans = dummy
        over = 0
        
        while l1 or l2 or over > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + over
            over = total // 10
            ans.next = ListNode(total % 10)
            
            ans = ans.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

        