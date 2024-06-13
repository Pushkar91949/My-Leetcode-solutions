# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = head
        r = head

        for i in range(k-1):
            r = r.next

        r2 = r

        while r.next:
            r = r.next
            l = l.next
        r2.val, l.val = l.val, r2.val 
        return head
    # Question link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
