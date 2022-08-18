# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        Logic: Counter
        
        Time: O(n*logn)
        Space: O(n)
        """
        counter = collections.Counter(arr)
        counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        
        removed = 0
        final_set_size = 0
        
        for k, v in counter.items():
            removed += v
            final_set_size += 1
            if removed >= len(arr) // 2:
                break
                
        return final_set_size
