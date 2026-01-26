"""Binary search =
👉 “Middle-la irundhu search pannum smart trick”"""


"""Search pannumbodhu:

Ellathaiyum one-by-one paakka maatta ❌

Half-half-aa cut pannite correct answer-ku pogum ✔️"""


"""📖 Phone book example

Imagine:

Phone book romba periya book 📕

Name K-la start aagudhu

❌ Stupid way:

A-la start panni

B, C, D… ellam paathukitte K varra varaikum flip pannradhu 😫

✔️ Smart way:

Middle page open pannuva

“Idhu K-ku munnaalaa / appuramaa?” nu check pannuva

Half pages-ai throw pannuva 🗑️

👉 Idhu thaan binary search"""


# Example
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print("Checking Index:", mid, "Value:", arr[mid])

        if arr[mid] == target:
            print("Found!")
            return mid

        elif arr[mid] < target:
            print("Too big, go left!")
            low = mid + 1

        else:
            print("Too small, go right!")
            high = mid - 1

    print("Not found!")
    return None

binary_search([10, 20, 30, 40, 50, 60], 40)