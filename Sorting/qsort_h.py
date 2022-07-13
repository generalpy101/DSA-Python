# faster than lomuto partition
def hoare(arr, l, h) -> int:
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


def qsort(arr, l, h) -> None:
    if l < h:
        p = hoare(arr, l, h)
        qsort(arr, l, p)
        qsort(arr, p+1, h)


l = [1, 3, 2, 4, 8, 7, 5, 10]
print(f"Original arr : {l}")
qsort(l,0,len(l) - 1)
print(f"Sorted arr : {l}")