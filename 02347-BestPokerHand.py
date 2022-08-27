class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        """
        Logic: Hash Set / Counter
        
        Time: O(n)
        Space: O(n)
        """
        poker_rank = {3: 3, 2: 2, 1: 1}
        poker_suit = {5: 4}
        rank_points = collections.Counter(ranks)
        suit_points = collections.Counter(suits)
        max_point = 1
        
        for point in rank_points.values():
            if point > 3: point = 3
            max_point = max(max_point, poker_rank[point])
            
        for point in suit_points.values():
            if point < 5: continue
            max_point = max(max_point, poker_suit[point])
                        
        if max_point == 4: return "Flush"
        elif max_point == 3: return "Three of a Kind"
        elif max_point == 2: return "Pair"
        else: return "High Card"
