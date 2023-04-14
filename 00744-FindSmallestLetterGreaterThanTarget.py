# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        curr_min_letter = letters[0]
        min_dist = float("inf")

        for ch in letters:
            if ord(ch)-ord(target) > 0:
                if min_dist > ord(ch)-ord(target):
                    curr_min_letter = ch
                    min_dist = ord(ch)-ord(target)
        
        return curr_min_letter
