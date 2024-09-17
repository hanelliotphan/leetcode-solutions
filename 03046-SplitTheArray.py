class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        """
        Logic: Intuitive brute force

        Time: O(n)
        Space: O(n)
        """
        return all(freq <= 2 for freq in collections.Counter(nums).values())
