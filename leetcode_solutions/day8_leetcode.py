class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_lis = [1]*n

        
        prefix = 1
        for x in range(n):
            new_lis[x] = prefix
            prefix *= nums[x]
        
        suffix = 1
        for x in range(n-1,-1,-1):
            new_lis[x] *= suffix
            suffix *= nums[x]

        return new_lis
            



