#https://www.youtube.com/watch?v=MZaf_9IZCrc
def lomuto(arr,l,r) :
    pivot = arr[r]
    i = l - 1
    for j in range(l,r) :
        if arr[j] < pivot :
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1] , arr[r] = arr[r], arr[i+1]
    return i + 1

l = [10,80,30,90,50,70]
print(f"Arr before partition : {l}")
print(f"i : {lomuto(l,0,len(l) - 1)}")
print(f"Arr after partition : {l}")