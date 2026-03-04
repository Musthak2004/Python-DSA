def solutionSearch(arr, item):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            start = mid + 1
        else:
            start = mid + 1

    return -1

print(solutionSearch([1, 2, 3, 4, 5], 2))
print(solutionSearch([1, 2, 3, 4, 5], 3))