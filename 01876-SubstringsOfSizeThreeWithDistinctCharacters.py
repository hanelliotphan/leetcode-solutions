# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        count = 0
        
        for i in range(len(s)-2):
            visited = set()
            substring = s[i:i+3]
            flag = 0
            for ch in substring:
                if ch not in visited:
                    visited.add(ch)
                else:
                    flag = 1
                    break
            if flag == 1: continue
            else: count += 1
                
        return count
