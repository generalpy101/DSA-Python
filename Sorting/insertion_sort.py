# Best : O(n) Worst : O(n^2)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr


if __name__ == "__main__":
    arr = [4, 42, 7, 1, 7, 7, 9, 2, 6, 4]
    print(f"Array before sorting : {arr}")
    insertion_sort(arr)
    print(f"Array after sorting : {arr}")