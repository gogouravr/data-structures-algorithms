class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            else:
                p *= i

        if zeros == 0:
            return [(p//n) for n in nums]
        
        if zeros == 1:
            return [0 if n!=0 else p for n in nums]



        return [0] * len(nums)