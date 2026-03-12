class Solution(object):
    def runningSum(self, nums):
        result = []
        current_sum = 0

        for i in nums:
            current_sum += i
            result.append(current_sum)

        return result

obj = Solution()
nums = [1, 2, 3, 4]
print(obj.runningSum(nums))
