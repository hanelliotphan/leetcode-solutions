# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        Logic: Linear Scan

        Time: O(n)
        Space: O(1)
        """
        curr_max = arr[0]
        max_index = 0
        
        for i in range(1, len(arr)):
            if curr_max < arr[i]:
                curr_max = arr[i]
                max_index = i
                
        return max_index
