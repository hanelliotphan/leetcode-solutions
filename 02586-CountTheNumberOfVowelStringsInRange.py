# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        for i in range(left, right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count
