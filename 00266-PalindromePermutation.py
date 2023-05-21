# https://leetcode.com/problems/palindrome-permutation/description/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(s)
        count = 0

        for v in counter.values():
            count += v % 2
        
        return count < 2
