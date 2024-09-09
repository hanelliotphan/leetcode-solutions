class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Logic: Sorting

        Time: O(n*logn)
        Space: O(n)
        """
        return sum(x != y for x, y in zip(heights, sorted(heights)))
