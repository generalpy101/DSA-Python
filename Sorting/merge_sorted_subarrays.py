'''
Problem : We are given 3 indices, low,mid and high and an array where 
elements are sorted from low to mid and then from mid+1 to high. We have to merge
elements between low and high inside the array itself so that elements inside
the range low to high are sorted. mid can be equal to low too.
Eg : [0,12,20,4,7] -> here low = 0, mid = 2, high = 4. Merged result will be 
[0,4,7,12,20] -> Here completely sorted array. low <= mid < high

We will first create 2 new lists which will contain items between low to mid and 
mid+1 to high respectively. Then we will apply same logic as we applied with merging 
two sorted arrays but this time we will replace the original list i.e we will have a 
new pointer k which will start from low and go all the way to high.
'''

def merge_subarray(arr,low,mid,high) :
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
        
arr = [0,2,20,13,15]
merge_subarray(arr,0,2,4)
print(arr)