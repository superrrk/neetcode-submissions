class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """ 2-pointer to select each bar height
        calculate the area by multiplying the max height and width
        store the largest bar height 
        get the width: count how far each bar is from each other using
        dict keys
        store the max area in a var, continue through the pointers until
        max gets updated and l == r 
        """

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r: 
            width = r - l
            cur_area = width * min(heights[l], heights[r])
            max_area = max(max_area, cur_area)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -=1
                
        return max_area


    
    

        
        
