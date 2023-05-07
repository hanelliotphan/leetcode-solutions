# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        curr_max = -1

        for i in range(len(arr)-1, -1, -1):
            arr[i], curr_max = curr_max, max(arr[i], curr_max)
        
        return arr
