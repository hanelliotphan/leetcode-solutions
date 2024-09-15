class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        Logic: Sorting by String

        Time: O(n*logn)
        Space: O(n)
        """
        return sorted(range(1, n+1), key=str)
