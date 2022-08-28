class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(min(nums))
        Space: O(1)
        """
        mn = min(nums)
        mx = max(nums)
        
        if mx % mn == 0: return mn
        
        for i in range(mn, 0, -1):
            if mn % i == 0 and mx % i == 0:
                return i
            
        return 1
