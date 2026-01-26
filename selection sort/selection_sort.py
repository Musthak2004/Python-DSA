"""
🧠 Selection Sort steps (ELI10)

1️⃣ Smallest element find pannu
2️⃣ First position-ku move pannu
3️⃣ Remaining list-la repeat 
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

numbers = [5, 3, 6, 2, 10]
print(selection_sort(numbers))