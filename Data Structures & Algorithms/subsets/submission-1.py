class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []
        def rec(i):
            if i == len(nums):
                res.append([*arr])
                return
            
            arr.append(nums[i])
            rec(i+1)
            arr.pop()
            rec(i+1)

        rec(0)

        return res
            
        