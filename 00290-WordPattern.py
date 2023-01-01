class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Logic: Hash Map
        
        Time: O(n)
        Space: O(n)
        """        
        s_list = s.split() # split string into list of separate words
        lookup = {} # hash map, key=pattern[i], val=s_list[i]
        
        # Base case: if size of pattern and s_list do not match, return False
        if len(pattern) != len(s_list):
            return False
        
        # Loop through each character of pattern
        for i in range(len(pattern)):
            # if such character
            # has not been visited and corresponding string in s_list
            # has not been stored as value in lookup, update lookup
            if pattern[i] not in lookup and s_list[i] not in lookup.values():
                lookup[pattern[i]] = s_list[i]
            # if pattern has not been visited but corresponding string 
            # in s_list has been in lookup, return False
            elif pattern[i] not in lookup and s_list[i] in lookup.values():
                return False
            # if the character in pattern and corresponding string in s_list
            # do not match, return False
            elif lookup[pattern[i]] != s_list[i]:
                return False
        
        # For each character in pattern, add the corresponding string
        # to constructed_string array
        constructed_string = []
        for p in pattern:
            constructed_string.append(lookup[p])
        
        # Return if the constructed_string and s_list are the same
        return constructed_string == s_list
