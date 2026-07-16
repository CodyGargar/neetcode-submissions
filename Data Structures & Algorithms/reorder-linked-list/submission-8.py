# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
            temp = head
            prev = None
            while(temp):
                temp2 = temp.next
                temp.next = prev
                prev = temp
                temp = temp2

            return prev
        def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            ans = temp = ListNode()
            first = True
            while(list1 and list2):
                if(first):
                    ans.next = list1
                    list1 = list1.next
                    first = not first
                else:
                    ans.next = list2
                    list2 = list2.next
                    first = not first
                ans = ans.next

            ans.next = list1 or list2

            return temp.next
            
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        head2 = reverseList(head2)

        mergeTwoLists(head,head2)




        
