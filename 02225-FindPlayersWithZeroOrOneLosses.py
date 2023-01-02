# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Logic: Hash Map
        
        Time: O(n*logn)
        Space: O(n)
        """
        loser_map = {}
        
        for winner, loser in matches:
            if loser not in loser_map:
                loser_map[loser] = 1
            else:
                loser_map[loser] += 1
            if winner not in loser_map:
                loser_map[winner] = 0
        
        win_all = []
        lose_once = []
        
        for k, v in loser_map.items():
            if v == 0:
                win_all.append(k)
            if v == 1:
                lose_once.append(k)
                
        win_all.sort()
        lose_once.sort()
        
        return [win_all, lose_once]
