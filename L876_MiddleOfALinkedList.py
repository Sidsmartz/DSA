# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

        #O(n) Time Complexity
        #O(1) Space Complexity

        #Same Complexities as using a counter to find the middle value.

#Using slow fast as its a convenient algorithm that might come up in the future