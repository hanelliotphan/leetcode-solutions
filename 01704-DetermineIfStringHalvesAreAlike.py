class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Logic: Brute Force
        
        Time: O(n)
        Space: O(n)
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        fm = sm = 0
        mid = len(s) // 2
        
        for i in range(len(s)):
            if i < mid and s[i] in vowels:
                fm += 1
            elif i >= mid and s[i] in vowels:
                sm += 1
        
        return True if fm == sm else False
