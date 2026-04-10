class Solution:
    def trap(self, h: List[int]) -> int:


        l = 0
        r = len(h) - 1
        lMax = h[l]
        rMax = h[r]
        res = 0

        while l < r:
            print(l,r)
            if h[l] < h[r]:
                l += 1
                lMax = max(h[l],lMax)
                res += lMax - h[l]
            else:
                r -= 1
                rMax = max(h[r],rMax)
                res += rMax - h[r]



        return res

        