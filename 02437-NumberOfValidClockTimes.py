# https://leetcode.com/problems/number-of-valid-clock-times/description/

class Solution:
    def countTime(self, time: str) -> int:
        """
        Logic: Brute Force
        
        Time: O(1)
        Space: O(1)
        """
        h, m = time.split(":")
        count_h = count_m = 0

        if h[0] == "?":
            if h[1] == "?":
                count_h += 24
            else:
                if int(h[1]) <= 3:
                    count_h += 3
                else:
                    count_h += 2
        elif h[1] == "?":
            if h[0] == "2":
                count_h += 4
            else:
                count_h += 10

        if m[0] == "?":
            if m[1] == "?":
                count_m += 60
            else:
                count_m += 6
        elif m[1] == "?":
            count_m += 10
        
        if not count_h and not count_m: return 1
        if not count_m: return count_h
        if not count_h: return count_m
        else: return count_h * count_m
