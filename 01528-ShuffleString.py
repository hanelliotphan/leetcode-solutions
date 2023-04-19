# https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        res = [""] * len(s)
        j = 0

        for i in indices:
            res[i] = s[j]
            j += 1
        
        return "".join(res)
