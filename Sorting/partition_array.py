'''
Problem : We are given an index and an array. We have to rearrange the array
such that all elements less than or equal to the element at index are to the 
left of index and all elements greater than the index element are to the right.
Order of elements at left or right doesn't matters.

Eg : [3,8,6,12,10,7] index = 5 will result in 
[3,6,7,8,12,10] or many of its variants.

Approach : move index element to the end of list. Then first move elements smaller
or equal to the element at index to another temp list. Then do same fore greater elements.
After that just copy temp to orignal array. We moved index element to end to tackle cases like
[1,4,8,5,12] where index is 2. Here if we will not move index element to end, 5 will come after 8.
We want index element to be the last smaller or equal element.

Time complexity : O(n), space complexity : O(n)
''' 

def partition(arr, index) :
    temp = []
    n = len(arr)
    arr[index],arr[n-1] = arr[n-1], arr[index]

    #smaller elements and the element itself is pushed
    for i in arr :
        if i <= arr[n-1] :
            temp.append(i)
    
    #larger elements are pushed
    for i in arr :
        if i > arr[n-1] :
            temp.append(i)

    for i in range(n) :
        arr[i] = temp[i]

l = [5,13,6,9,12,8,11]
print(f"Before partition : {l}")
partition(l,5)
print(f"After partition : {l}")