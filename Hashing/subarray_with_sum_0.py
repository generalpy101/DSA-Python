'''
Find subarray with sum 0, subarray has contiguous elements
    eg : in arr [1,-2,1,4,2] subarray with sum 0 is [1,-2,1]
    (not that [-2,4,2] is not contiguous so not included)
    Our function here would return True
    
Will use prefix sum + hashing
'''

def zero_sum_sub_array(arr) :
    s = set()
    prefix_sum = 0
    for i in range(len(arr)) :
        prefix_sum += arr[i]
        if prefix_sum == 0 or prefix_sum in s :
            return True
        s.add(prefix_sum)
    return False

if __name__ == '__main__':
    print(zero_sum_sub_array([1,-2,1,4,2]))
    print(zero_sum_sub_array([1,-2,4,2]))
    print(zero_sum_sub_array([3,-1,-2]))