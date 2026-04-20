class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp= {}
        def lis(i: int = 0):
            if i in dp:
                return dp[i]

            res = 1
            for j in range(i+1,len(nums)):
                res = max(res, int(nums[j] > nums[i]) + lis(j))

            dp[i] = res
            return res

        
        dp2 = [1]*(len(nums))

        for i in range(1,len(nums)):
            max_len = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len,dp2[j])

            dp2[i] += max_len
        print(dp2)
        return max(dp2)




                

        