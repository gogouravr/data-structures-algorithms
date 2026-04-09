class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = prices[-1]
        res = 0

        for i in range(len(prices)-1 , -1,-1):
            res = max(res,maxVal-prices[i])
            maxVal = max(maxVal, prices[i])

        return res
        
        