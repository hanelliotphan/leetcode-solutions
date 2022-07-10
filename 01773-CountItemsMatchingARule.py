class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Logic: Decode rule key
        
        Time: O(n)
        Space: O(1)
        """
        code = -1
        if ruleKey == "type": code = 0
        elif ruleKey == "color": code = 1
        else: code = 2
            
        count = 0
        
        for item in items:
            if item[code] == ruleValue:
                count += 1
                
        return count
