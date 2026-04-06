class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        res = 0
        dp = {}
        def rec(target,i):
            # print(target,i)
            # if i == len(coins):

            if (target,i) in dp:
                return dp.get((target,i))

            if target == 0:
                return 1
            
            if target < 0:
                return 0


            if len(coins) == i:
                return 0
            
            dp[(target,i)] =  rec(target-coins[i],i) + rec(target,i+1)
            return dp[(target,i)]


        return rec(amount,0)
        # return res

        

        