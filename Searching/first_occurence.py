"""
Problem : Find first occurence of an element in an array
We will use modified binary search for that.
"""


def first_occurence(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < item:
            low = low + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != item:
                return mid
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10, 10, 11, 23]
    item = 10
    print(first_occurence(arr, item))  # 5
