# https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        Logic: Hash Map with Sort
        
        Time: O(n*logn)
        Space: O(n)
        """
        score_copy = score[::]
        score_copy.sort(reverse=True)
        ranks = dict()
        i = 1

        for s in score_copy:
            ranks[s] = i
            i += 1
        
        for k, v in ranks.items():
            if v == 1:
                ranks[k] = "Gold Medal"
            elif v == 2:
                ranks[k] = "Silver Medal"
            elif v == 3:
                ranks[k] = "Bronze Medal"
        
        return [str(ranks[x]) for x in score]
