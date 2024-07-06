# https://leetcode.com/problems/product-of-array-except-self/editorial/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return withprefixandsuffixarrays(nums)

def withprefixandsuffixarrays(nums: List[int]) -> List[int]:
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)

    for i in range(len(nums)):
        if i != 0:
            prefix[i] *= prefix[i-1] * nums[i-1]
    
    for i in reversed(range(len(nums))):
        if i != len(nums)-1:
            suffix[i] *= suffix[i+1] * nums[i+1]
    
    return [prefix[i]*suffix[i] for i in range(len(nums))]


def noZeros(nums):
    totalMultiple = nums[0]
    for i in range(1, len(nums)):
        totalMultiple *= nums[i]
    return [int(totalMultiple/x) for x in nums]
        
