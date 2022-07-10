# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Logic: Slow-Fast approach

        Time: O(n)
        Space: O(1)
        """
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
