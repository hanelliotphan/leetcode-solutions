class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        """
        Logic: Recursion
        
        Time: O(n)
        Space: O(1) -- replace the same `nums` list
        """
        def helper(n):
            if n == 1:
                return
            for i in range(n//2):
                if i % 2:
                    nums[i] = max(nums[i*2], nums[i*2+1])
                else:
                    nums[i] = min(nums[i*2], nums[i*2+1])
            helper(n//2)
            return
        
        helper(len(nums))
        return nums[0]
