# https://leetcode.com/problems/counting-elements/description/

class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        counter = collections.Counter(arr)
        res = 0

        for n in arr:
            if counter[n+1]:
                res += 1
        
        return res
