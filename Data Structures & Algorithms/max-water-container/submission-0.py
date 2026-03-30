class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        l = 0
        r = n-1
        
        while l<r:
            width = r-l
            height = min(heights[l], heights[r])
            area = max(area, height*width)


            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return area
