# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumOptimizedMap(nums, target)
    
    def twoSumBF(self, nums: List[int], target: int) -> List[int]:
        # BRUTE FORCE SOLUTION
        sze_nums = len(nums)
        for i in range(sze_nums):
            for j in range(sze_nums):
                if target==nums[i]+nums[j] and i!=j:
                    return [i,j]
        return []
    
    def twoSumOptimizedMap(self,nums: List[int], target: int) -> List[int]:
        # twoSumOptimizedMap
        sze_nums = len(nums)
        numMap ={}
        for i in range(sze_nums):
            numMap[nums[i]] = i
        # print(numMap)
        for i in range(sze_nums):
            # print((target - nums[i] in numMap), nums[i], target - nums[i])
            if (target - nums[i] in numMap) and numMap[target - nums[i]]!=i:
                return [i, numMap[target - nums[i]]]
        return []
        

    
        
