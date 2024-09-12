class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        """
        Logic: Hash set with Brute Force intuition

        Time: O(n)
        Space: O(1)
        """
        hash_set = set()

        for i in range(len(s)-1):
            if s[i] == s[i+1] or s[i:i+2][::-1] in hash_set:
                return True
            hash_set.add(s[i:i+2])

        return False
