class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        Logic: Sort

        Time: O(n*logn)
        Space: O(1)
        """
        weight.sort()
        res = count = 0

        for w in weight:
            if res >= 5000:
                break
            else:
                res += w
                count += 1
        
        return count if res <= 5000 else count-1
