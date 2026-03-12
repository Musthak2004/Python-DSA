class Solution(object):
    def twoSum(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low < high:
            sum = nums[low] + nums[high]
            if sum == target:
                return [low, high]
            elif sum < target:
                low += 1
            else:
                high -= 1

        return []

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))