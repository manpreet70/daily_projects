class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numslen = len(nums)
        max_reach = 0

        for i in range(numslen):
            if i > max_reach:
                return False
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
                
        return True
