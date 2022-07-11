def merge(arr,low,mid,high) :
    la = arr[low:mid+1]
    lb = arr[mid+1:high+1]
    m = len(la)
    n = len(lb)

    i = 0
    j = 0
    k = low

    while i < m  and j < n :
        if la[i] < lb[j] :
            arr[k] = la[i]
            i+=1
            k+=1
        else :
            arr[k] = lb[j]
            j+=1
            k+=1
    
    while i < m :
        arr[k] = la[i]
        i+=1
        k+=1

    while j < n :
        arr[k] = lb[j]
        j+=1
        k+=1

def mergeSort(arr,l,r):
    if r > l :
        m = (l+r) // 2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

arr = [4,2,1,65,22,6,8]
mergeSort(arr,0,len(arr) - 1)
print(arr)

#Time complexity O(nlogn)
#Space complexity O(n) -> Due to merge fn using extra arrays and recursion