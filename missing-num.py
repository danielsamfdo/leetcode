# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for idx, num in enumerate(nums):
            x += (idx)-num
        x += len(nums)
        return x
