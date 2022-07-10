class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Logic: List Slicing
        
        Time: O(n)
        Space: O(n)
        """
        n = len(chars)
        slice_indices = [0]
        
        for i in range(n-1):
            if chars[i] != chars[i+1]:
                slice_indices.append(i+1)
                
        slice_indices.append(n)

        for j in range(1, len(slice_indices)):
            chars.append(chars[slice_indices[j]-1])
            count = len(chars[slice_indices[j-1] : slice_indices[j]])
            if count > 1:
                count = str(count)
                for d in count:
                    chars.append(d)
                    
        i = 0
        while i < n:
            chars.pop(0)
            i += 1
            
        return len(chars)
