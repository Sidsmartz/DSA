# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        #One 'pointer' goes 2 nodes one goes 1 node forward.
        #If they meet, cycle exists

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        
        #If loop is over, List is limited so no cycles
        return False
        
#Nothing is stored in memory so Space Complexity is O(1)
#Time Complexity is O(n) as we iterate through the list once

#Better than the O(n), O(n) solution where a hashmap is used to store the node references
#and before adding a new node to the hashmap, we check if its already in the hashmap
