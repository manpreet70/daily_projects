# Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for element in nums:
            if count == 0:
                candidate = element
            if element == candidate:
                count += 1:
            else:
                count -= 1

        return candidate

            