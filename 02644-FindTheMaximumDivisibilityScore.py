# https://leetcode.com/problems/find-the-maximum-divisibility-score/description/

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        """
        Logic: Brute Force

        Time: O(n*d)
        Space: O(n)
        """
        max_div_score = float('-inf')
        max_div = -1

        for d in divisors:
            count = 0
            for n in nums:
                if n % d == 0:
                    count += 1
            if count > 0:
                if count == max_div_score:
                    max_div = min(max_div, d)
                elif count > max_div_score:
                    max_div = d
            max_div_score = max(max_div_score, count)
        
        return max_div if max_div > -1 else min(divisors)
