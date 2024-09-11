class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Logic: XOR operation

        Time: O(start^goal) -- count()
        Space: O(1)
        """
        xor = start ^ goal
        return bin(xor).count('1')
