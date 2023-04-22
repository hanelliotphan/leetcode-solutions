# https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        count = 0
        num_s = str(num)
        
        for i in range(len(num_s)-k+1):
            if int(num_s[i:i+k]) != 0 and num % int(num_s[i:i+k]) == 0:
                count += 1
        
        return count
