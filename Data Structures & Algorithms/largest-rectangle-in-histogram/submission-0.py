class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        best = 0
        n = len(heights)

        for i in range(n+1):
            h = heights[i] if i < n else 0
            start = i

            while stack and stack[-1][1]>h:
                idx,height_popped = stack.pop()
                best = max(best,height_popped*(i-idx))
                start = idx
            stack.append((start,h))
        return best


 #so there are bars 1,2,3,4..
       #we have return area of a biggest rectangle that can be formed
       #by brute force you start with the first height if next height is taller width increases
       #you do it for every rectangle

