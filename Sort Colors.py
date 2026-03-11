class Solution(object):
    def sortColors(self, nums):
        n = len(nums)

        for i in range(n):
            smallest = i

            for j in range(i+1, n):
                if nums[j] < nums[smallest]:
                    smallest = j

            nums[smallest], nums[i] = nums[i], nums[smallest]

        return nums

obj = Solution()
nums = [2,0,1]
print(obj.sortColors(nums))