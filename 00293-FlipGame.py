# https://leetcode.com/problems/flip-game/description/

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(1) --> need to return `res`, no extra space needed in the implementation
        """
        res = list()

        for i in range(len(currentState)-1):
            if currentState[i:i+2] == "++":
                res.append(currentState[:i]+"--"+currentState[i+2:])
        
        return list(set(res))
