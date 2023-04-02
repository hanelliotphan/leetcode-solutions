# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        """
        Logic: String expansion

        Time: O(n)
        Space: O(1)
        """
        if len(set(s)) == 1:
            return 0

        sub_s = "01"
        
        while sub_s in s:
            sub_s = f"0{sub_s}1"
        
        return len(sub_s)-2 # minus 2 because sub_s has been concatenated with 0 and 1 at the last loop
