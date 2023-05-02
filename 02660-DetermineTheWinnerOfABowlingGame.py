# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1)
        """
        flag1 = flag2 = False
        i1 = i2 = -1
        score1 = score2 = 0

        for i in range(len(player1)):
            if flag1 and i-i1 <= 2:
                score1 += 2*player1[i]
            else:
                score1 += player1[i]
            if player1[i] == 10:
                flag1 = True
                i1 = i
        
        for i in range(len(player2)):
            if flag2 and i-i2 <= 2:
                score2 += 2*player2[i]
            else:
                score2 += player2[i]
            if player2[i] == 10:
                flag2 = True
                i2 = i
        
        if score1 == score2:
            return 0
        elif score1 > score2:
            return 1
        return 2
