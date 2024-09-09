class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        """
        Logic: Linear Scanning

        Time: O(s)
        Space: O(k)
        """
        curr_word = ""
        res = ""
        knowledge_d = {k: v for k, v in knowledge}
        is_replacing = False

        for ch in s:
            if ch == "(":
                is_replacing = True
            elif ch == ")":
                if curr_word in knowledge_d:
                    res += knowledge_d[curr_word]
                else:
                    res += "?"
                curr_word = ""
                is_replacing = False
            elif is_replacing:
                curr_word += ch
            else:
                res += ch
        
        return res
