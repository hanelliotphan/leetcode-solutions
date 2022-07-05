class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Logic: Hashmap of visited indices
            - If character already visited and current index
        shows that the character is just new, jump to next char
            - Else, update max_length of all the characters
        just visited
            - Then, update index of visited character
        
        Time: O(n)
        Space: O(n)
        """
        start_idx, max_len = 0, 0
        visited = {}
        
        for i in range(len(s)):
            if s[i] in visited and start_idx <= visited[s[i]]:
                start_idx = visited[s[i]] + 1
            else:
                max_len = max(max_len, i-start_idx+1)
            visited[s[i]] = i
            
        return max_len
