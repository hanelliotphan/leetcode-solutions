class Solution:
    def countElements(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        mx = max(nums)
        mn = min(nums)
        count = 0
        
        for n in nums:
            if n != mx and n != mn and mx > n > mn:
                count += 1
                
        return count
