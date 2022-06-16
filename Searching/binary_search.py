# A sorted array is required


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item: 
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binary_search_r(arr, item, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == item:
        return mid
    if arr[mid] > item:
        return binary_search_r(arr, item, low, high - 1)
    else :
        return binary_search_r(arr, item, low + 1, high)


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10, 11, 23]
    item = 20
    print(binary_search(arr, item))#-1
    print(binary_search_r(arr, item,0,len(arr) - 1))#-1
