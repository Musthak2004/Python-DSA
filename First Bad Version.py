# Simulate API locally for testing
BAD_VERSION = 4
def isBadVersion(version):
    return version >= BAD_VERSION

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n

        while low < high:
            mid = (low + high)//2
            if isBadVersion(mid):
                high = mid   # move left
            else:
                low = mid + 1 # move right

        return low  # first bad version

n = 5
obj = Solution()
print(obj.firstBadVersion(n))  # Output: 4