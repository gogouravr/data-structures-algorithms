class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # res = 0
        # dp = {}
        # def rec(target,i):
        #     # print(target,i)
        #     # if i == len(coins):

        #     if (target,i) in dp:
        #         return dp.get((target,i))

        #     if target == 0:
        #         return 1
            
        #     if target < 0:
        #         return 0


        #     if len(coins) == i:
        #         return 0
            
        #     dp[(target,i)] =  rec(target-coins[i],i) + rec(target,i+1)
        #     return dp[(target,i)]


        # return rec(amount,0)
        # # return res

        

        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            coin = coins[i-1]
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j] + (dp[i][j-coin] if j >= coin else 0)

        # print(dp)
        return dp[n][amount]