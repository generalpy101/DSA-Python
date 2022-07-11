"""
Problem : Merge 2 sorted lists
Use 2 pointers, since lists are sorted, keep moving pointers accordingly.
Compare elements, if item in list 1 is greater then increase first pointer
and push value, else increase second pointer and push it.
"""

def merge_sorted_lists(list1, list2):
    res = []
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        if list1[i] < list2[j] :
            res.append(list1[i])
            i += 1
        else :
            res.append(list2[j])
            j += 1
        
    while i < n :
        res.append(list1[i])
        i += 1
    
    while j < m :
        res.append(list2[j])
        j += 1
    
    return res

print(merge_sorted_lists([1,2,4,9], [0,3,11,12]))