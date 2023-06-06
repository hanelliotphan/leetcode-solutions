# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Logic: Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        arr.sort()
        diff = abs(arr[1]-arr[0])
        
        for i in range(1, len(arr)-1):
            if abs(arr[i+1]-arr[i]) != diff:
                return False
            
        return True
