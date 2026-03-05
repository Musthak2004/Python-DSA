class Solution(object):
    def searchRange(self, nums, target):

        # -------- First Position --------
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1      # move left
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        # -------- Last Position --------
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1       # move right
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [first, last]


nums = [5,7,7,8,8,10]
obj = Solution()
print(obj.searchRange(nums, 8))