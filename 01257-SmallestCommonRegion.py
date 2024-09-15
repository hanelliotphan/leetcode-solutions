class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        """
        Logic: Hash Set for Common Ancestors

        Time: O(n)
        Space: O(n)
        """
        region_parents = dict()
        nodes = {region1}

        for region in regions:
            for sub_region in region[1:]:
                region_parents[sub_region] = region[0]
        
        while region1 in region_parents:
            region1 = region_parents[region1]
            nodes.add(region1)
        
        while region2 not in nodes:
            region2 = region_parents[region2]
        
        return region2
