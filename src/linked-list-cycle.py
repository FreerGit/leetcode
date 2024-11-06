# This abuses the fact that the number of nodes is with the range [0, 10^4]
# so if we have not encountered a null node before that, we must be in a cycle.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = 0
        node = head
        while node != None:
            if seen > 10000:
                return True
            node = node.next
            seen += 1

        return False
    
# Another solution I saw was doing the two pointer thingy
# if the two pointers ever point at the same *object* then it's a cycle.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False