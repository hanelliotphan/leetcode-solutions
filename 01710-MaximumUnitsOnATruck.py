# https://leetcode.com/problems/maximum-units-on-a-truck/description/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Logic: Brute Force with Sort
        
        Time: O(n*logn)
        Space: O(1)
        """
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        curr_boxes = curr_units = 0

        for boxes, units in boxTypes:
            if curr_boxes == truckSize:
                break
            possible_boxes = min(boxes, truckSize-curr_boxes)
            curr_units += units*possible_boxes
            curr_boxes += possible_boxes
        
        return curr_units
