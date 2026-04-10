class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         res = max(res , (j-i)*min(heights[i],heights[j]))

        l = 0 
        r = n - 1

        while l < r:
            res = max(res, (r-l)*min(heights[r],heights[l]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return res
        