"""
Problem : Count all occurences of an element in an array
We will use modified binary search for that.
"""


def count_occurence(arr, item):
    count = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < item:
            low = low + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            count += 1
            i = mid - 1
            while arr[i] == item:
                count += 1
                i -= 1
            j = mid + 1
            while arr[j] == item:
                count += 1
                j += 1
            break

    return count


'''
Another solution :
find first occurence
    if first occurence is 0:
        return 0
    else :
        return last occurence - first occurence + 1
        
Time Complexity : O(logn + logn) = O(logn)
'''


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10, 10, 10, 11, 23]
    item = 10
    print(count_occurence(arr, item))  # 6 ; O(logn + k)
