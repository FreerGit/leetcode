# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next     # save next before we overwrite it
            curr.next = prev   # flip the pointer
            prev = curr        # advance prev
            curr = nxt         # advance curr
        return prev