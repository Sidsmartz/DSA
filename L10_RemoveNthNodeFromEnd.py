# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy

        for i in range(n+1):
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next

        return dummy.next
        
#Ahead 'pointer' is moved n+1 time
#Then both pointers are moved until ahead reaches the end
#This means behind is now n nodes from the end
#Behind is then moved one more node forward to remove the nth node from the end

#Time Complexity: O(n)
#Space Complexity: O(1)

