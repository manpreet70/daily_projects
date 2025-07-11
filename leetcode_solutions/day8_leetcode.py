# Day 8 LeetCode – Product of Array Except Self
# O(n) time, O(1) extra space (output list excluded)
from typing import List

# ─────────────────────────────────────────────────────────────
# Main solution class expected by LeetCode
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_lis = [1]*n

        # First pass: store prefix products in-place
        prefix = 1
        for x in range(n):
            new_lis[x] = prefix
            prefix *= nums[x]
        
        # Second pass: multiply by suffix products as we walk backwards
        suffix = 1
        for x in range(n-1,-1,-1):
            new_lis[x] *= suffix
            suffix *= nums[x]

        # new_lis now contains prefix * suffix for each index
        return new_lis
            



