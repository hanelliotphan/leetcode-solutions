class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        """
        Logic: Brute Force
        
        Time: O(n) --> n = number of digits in `num`
        Space: O(n)
        """
        n_s = str(num)
        count = 0
        
        for i in range(len(n_s)-k+1):
            if int(n_s[i:i+k]) != 0 and num % int(n_s[i:i+k]) == 0:
                count += 1
                
        return count
