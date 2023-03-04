# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1) --> return O(n) array is required, no extra is needed
        """
        res = [pref[0]]

        if len(pref) < 2:
            return res

        for i in range(1, len(pref)):
            res.append(pref[i-1]^pref[i])
        
        return res
