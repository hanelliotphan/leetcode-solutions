class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        """
        Logic: Brute Force

        Time: O(n)
        Space: O(1)
        """
        max_val = 0
        
        for s in strs:
            is_all_digit = True
            for ch in s:
                if not (48 <= ord(ch) <= 57):
                    max_val = max(max_val, len(s))
                    is_all_digit = False
                    break
            if is_all_digit:
                max_val = max(max_val, int(s))

        return max_val
