# https://leetcode.com/problems/best-poker-hand/description/

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        """
        Logic: Hash Map/Counter
        
        Time: O(r+s)
        Space: O(r+s)
        """
        rank_counter = collections.Counter(ranks)
        suit_counter = collections.Counter(suits)
        curr_best_rank = curr_best_suit = 1

        for k, v in rank_counter.items():
            curr_best_rank = max(curr_best_rank, v)

        for k, v in suit_counter.items():
            curr_best_suit = max(curr_best_suit, v)
        
        if curr_best_suit == 5:
            return "Flush"
        if curr_best_rank >= 3:
            return "Three of a Kind"
        if curr_best_rank >= 2:
            return "Pair"
        else:
            return "High Card"
