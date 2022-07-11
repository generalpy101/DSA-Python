#O(n^2)
def bubble_sort(arr) :
    for i in range(len(arr) - 1) :
        swapped = False
        for j in range(len(arr) - i - 1) :
            if arr[j] > arr[j + 1] :
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
                swapped = True
        if not swapped :
            return
    
if __name__ == '__main__':
    arr = [4,42,7,1,7,7,9,2,6,4]
    print(f"Array before sorting : {arr}")
    bubble_sort(arr)
    print(f"Array after sorting : {arr}")