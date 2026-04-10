class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idx = {}

        for i in range(len(nums)):
            idx[nums[i]] = [0,1]
        
        res = 0
        
        for i in range(len(nums)):
            if nums[i] in idx and idx[nums[i]][0] == 0:
                j = 1
                idx[nums[i]][0] = 1
                while nums[i] + j in idx and idx[nums[i]+j][0] == 0:
                    idx[nums[i]+j][0] = 1
                    j += 1

                if nums[i] + j in idx:
                    idx[nums[i]][1] = j + idx[nums[i] + j][1]
                else:
                    idx[nums[i]][1] = j 

                res = max(res,idx[nums[i]][1])

        return res
