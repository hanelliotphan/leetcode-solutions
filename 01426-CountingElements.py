# https://leetcode.com/problems/counting-elements/description/

class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        Logic: Hash Map/Counter
        
        Time: O(n)
        Space: O(n)
        """
        num_count = collections.Counter(arr)
        count = 0
        
        for n in arr:
            if num_count[n+1]:
                count += 1
        
        return count
