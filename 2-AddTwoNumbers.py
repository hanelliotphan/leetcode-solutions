# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Logic: Mathematical Approach with Carry Flag
        
        Time Complexity: O(max(m,n))
        Space Complexity: O(max(m,n))
        """    
        p = l1
        q = l2
        dummy = ListNode()
        carry = 0
        curr = dummy
        
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if p: p = p.next
            if q: q = q.next
                
        if carry > 0:
            curr.next = ListNode(carry)
                
        return dummy.next
