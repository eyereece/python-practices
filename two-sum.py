class Solution:
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[num] = i
        return []
    
nums = [2, 7, 11, 15]
target = 9

two_sum = Solution()
print(two_sum.twoSum(nums, target))