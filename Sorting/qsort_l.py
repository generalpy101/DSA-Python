def lomuto(arr,l,r) :
    pivot = arr[r]
    i = l - 1
    for j in range(l,r) :
        if arr[j] < pivot :
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1] , arr[r] = arr[r], arr[i+1]
    return i + 1

def qsort(arr,l, r) :
    if l < r :
        p = lomuto(arr,l,r)
        qsort(arr,l,p-1)
        qsort(arr,p+1,r)

l = [4,3,7,1,8,5,11,12]
print(f"Original arr : {l}")
qsort(l,0,len(l) - 1)
print(f"Sorted arr : {l}")