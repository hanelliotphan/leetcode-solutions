# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """
        hm = dict()
        l = 0
        longest = float("-inf")

        for i in range(len(s)):
            if s[i] in hm and hm[s[i]] >= l:
                l = hm[s[i]] + 1
            hm[s[i]] = i
            longest = max(longest, i-l+1)
        
        return longest if longest != float("-inf") else 0
