class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        nums = []
        
        for i in range(n):
            nums.append(start+2*i)
            
        xor = nums[0]
        for i in range(1, n):
            xor ^= nums[i]
            
        return xor
