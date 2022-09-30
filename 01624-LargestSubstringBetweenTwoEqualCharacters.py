# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Logic:
        
        Time:
        Space:
        """
        max_sub = 0
        twice_found = False
        visited = dict()
        
        for i in range(len(s)):
            if s[i] not in visited:
                visited[s[i]] = [i]
            else:
                visited[s[i]].append(i)
                twice_found = True
        
        if twice_found == False:
            return -1
        
        for k, v in visited.items():
            if len(v) == 1:
                continue
            max_sub = max(max_sub, v[-1]-v[0]-1)
        
        return max_sub
