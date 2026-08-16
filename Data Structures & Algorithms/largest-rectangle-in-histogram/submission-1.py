class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxarea=0
        for i in range(n):
            height=heights[i]
            r=i+1
            while r<n and heights[r]>=height:
                r+=1
            l=i
            while l>=0 and heights[l]>=height:
                l-=1
            r-=1
            l+=1
            maxarea=max(maxarea,height*(r-l+1))
        return maxarea