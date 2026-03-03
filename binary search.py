def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        guess = array[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [2,5,8,12,16,23,38,56,72,91]
print(binary_search(my_list, 50))