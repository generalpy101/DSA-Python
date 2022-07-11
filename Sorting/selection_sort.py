# O(n^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


if __name__ == "__main__":
    arr = [4, 42, 7, 1, 7, 7, 9, 2, 6, 4]
    print(f"Array before sorting : {arr}")
    selection_sort(arr)
    print(f"Array after sorting : {arr}")