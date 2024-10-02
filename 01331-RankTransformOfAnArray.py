class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Logic: Hash Set + Sorting

        Time: O(n*logn)
        Space: O(n)
        """
        ranks = {}
        curr_rank = 1

        for i in sorted(list(set(arr))):
            ranks[i] = curr_rank
            curr_rank += 1
        
        return [ranks[n] for n in arr]
