# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            

        sec_half=slow.next
        slow.next = None
        prev=None

        while sec_half:
            tmp = sec_half.next
            sec_half.next = prev
            prev= sec_half
            sec_half = tmp

        first_half = head # Second half reversed. Merge

        sec_half = prev # New head when reversed(End of list)

        while sec_half:
            tmp1= first_half.next
            tmp2=sec_half.next
            
            first_half.next = sec_half
            sec_half.next = tmp1

            first_half = tmp1
            sec_half = tmp2

        