class Solution(object):
    def runningSum(self, nums):
        result = []
        current = 0

        for num in nums:
            current = current + num
            result.append(current)
        return result

obj = Solution()
nums = [1, 2, 3, 4]
print(obj.runningSum(nums))
