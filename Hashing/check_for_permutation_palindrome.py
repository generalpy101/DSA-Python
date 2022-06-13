'''
Test if we can rearrange a string to get palindrome
    eg: loop will return false as there is no arrangement available with palindrome
    while geegg can be reaaranged to gegeg or eggge so it will return true
    
Answer is if there is a atmost 1 character with odd frequency we will get true else false.
Can also use counter. I will write counter code in comments
'''

#from Collections import Counter

def check_for_permutation(string) :
    d = dict()
    for i in string :
        if not d.get(i) :
            d[i] = 1
        else :
            d[i] += 1
    #with counter above code will be :
    #d = Counter(string)
    count = 0
    for j in d.values() :
        if j%2 != 0:
            count += 1
        if count > 1 : return False 
    return True

if __name__ == "__main__":
    print(check_for_permutation("loop"))#False
    print(check_for_permutation("geegg"))#True
    print(check_for_permutation("aabbc"))#True