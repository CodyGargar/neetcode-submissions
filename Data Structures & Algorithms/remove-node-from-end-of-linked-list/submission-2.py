# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = final =dummy = ListNode(0,head)
        size = 0
        for i in range(n+1):
            final = final.next
            size+=1

        while(final):
            curr = curr.next
            final = final.next
            size+=1
        
        curr.next = curr.next.next
        return dummy.next
