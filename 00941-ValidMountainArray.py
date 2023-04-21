# https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Logic: Brute Force (find the peak)
        
        Time: O(n)
        Space: O(1)
        """
        if len(arr) < 3:
            return False
        
        peak = 0

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                peak = i
                break
            elif arr[i] == arr[i+1]:
                return False

        if peak == 0:
            return False
        
        for i in range(peak, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        
        return True
