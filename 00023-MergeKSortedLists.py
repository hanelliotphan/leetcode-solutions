# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Logic: Brute Force

        Time: O(n logn)
        Space: O(n)
        """
        nodes = []
        head = dummy = ListNode(0)

        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        for node in sorted(nodes):
            dummy.next = ListNode(node)
            dummy = dummy.next
        
        return head.next
