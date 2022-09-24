class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        Logic: Sorting
        
        Time: O(n*logn)
        Space: O(1)
        """
        return sorted(target) == sorted(arr)
