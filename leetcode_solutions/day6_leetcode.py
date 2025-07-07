class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_end = 0
        jumps = 0

        for i in range(len(nums)-1):
            if farthest < i + nums[i]:
                farthest = i + nums[i]
            if i == current_end:
                jumps +=1
                current_end = farthest
        return jumps

        