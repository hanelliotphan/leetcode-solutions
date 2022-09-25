class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Logic: Hash Map
        
        Time: O(m+n)
        Space: O(m+n)
        """
        l1_indices = dict()
        l2_indices = dict()
        min_idx_sum = float("inf")
        new_common_strs = []
        
        for i in range(len(list1)):
            l1_indices[list1[i]] = i
            
        for i in range(len(list2)):
            l2_indices[list2[i]] = i
            
        for k, v in l1_indices.items():
            if k in l2_indices.keys():
                if min_idx_sum > v + l2_indices[k]:
                    min_idx_sum = v + l2_indices[k]
                    new_common_strs = [k]
                elif min_idx_sum == v + l2_indices[k]:
                    new_common_strs.append(k)
                    
        return new_common_strs
