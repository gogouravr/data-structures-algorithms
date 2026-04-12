class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s%2 == 1:
            return False

        def rec(i=0,reqSum=(s//2)):
            if reqSum == 0:
                return True
            if i == len(nums):
                return False

            return rec(i+1,reqSum - nums[i]) or \
            rec(i+1,reqSum)


        return rec()
