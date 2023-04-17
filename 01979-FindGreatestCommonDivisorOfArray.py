class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(min(nums))
        Space: O(1)
        """
        mn = min(nums)
        mx = max(nums)
        
        if mn == mx:
            return mn
            
        gcd = 1

        for i in range(1, mx+1):
            if i > mn:
                break
            if mx % i == 0 and mn % i == 0:
                gcd = max(gcd, i)
        
        return gcd
