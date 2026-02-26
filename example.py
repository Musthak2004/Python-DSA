def binary_search(arr, item):
    low = 0
    high = (len(arr)) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess