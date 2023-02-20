# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Logic: Binary Search
        
        Time: O(logn)
        Space: O(1)
        """    
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return l
