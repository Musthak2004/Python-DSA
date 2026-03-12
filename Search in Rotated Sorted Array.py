class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            