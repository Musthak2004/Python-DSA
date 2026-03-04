class Solution(object):
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return [mid]
            elif guess < target:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return [mid]
            elif guess < target:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]

nums = [5,7,7,8,8,10]
obj = Solution()
print(obj.searchRange(nums, 0))