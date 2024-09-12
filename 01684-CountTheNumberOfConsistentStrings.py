class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Logic: Hash Set

        Time: O(a + w * max(len(word)))
        Space: O(a) -- set(allowed)
        """
        count = 0

        for word in words:
            if all(ch in set(allowed) for ch in word):
                count += 1
        
        return count
