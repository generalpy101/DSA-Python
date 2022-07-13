# https://www.youtube.com/watch?v=AO8Sav4SmSU

'''
Unstable partition system
Doesn't guarantees that pivot will be at correct position
Eg : for [5, 3, 8, 4, 2, 7, 1, 10] output is 
[1, 3, 2, 4, 8, 7, 5, 10]
Here 5 must be after 4 but it is after 7
Elements are partitioned acc to 5 but 5 itself it is not 
partitioned correctly.
O(n)
'''


def hoare(arr, l, h):
    pivot = arr[l]  # here pivot is low

    i = l - 1
    j = h + 1

    while True:
        i = i+1
        while arr[i] < pivot:
            i = i + 1

        j = j-1
        while arr[j] > pivot:
            j = j-1

        if i >= j:
            return j

        arr[j], arr[i] = arr[i], arr[j]


l = [5, 3, 8, 4, 2, 7, 1, 10]
print(f"Before Partition : {l}")
print(hoare(l, 0, len(l) - 1))
print(f"After Partition : {l}")
