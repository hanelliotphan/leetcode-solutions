# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        Logic: Greatest Common Divisor
        
        Time: O(n*(logn)^2)
        Space: O(n)
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        counter = collections.Counter(deck)
        return reduce(gcd, counter.values()) > 1
