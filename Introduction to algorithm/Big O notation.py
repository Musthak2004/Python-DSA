# O(1) – Constant Time (Super fast ⚡)

def get_first_item(arr):
    return arr[0]

# -----------------------------------------------------

# O(n) – Linear Time

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

#-----------------------------------------------------

# O(log n) – Logarithmic Time (Binary Search 🚀)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

#---------------------------------------------------------

# O(n log n) – Fast Sorting

numbers = [5, 2, 9, 1, 3]
numbers.sort()

#-------------------------------------------------------

# O(n²) – Slow Algorithm 🐌

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

#--------------------------------------------------------

# O(n!) – Very Very Slow (Danger ⚠️)

import itertools

cities = ["A", "B", "C"]
routes = list(itertools.permutations(cities))
print(routes)
