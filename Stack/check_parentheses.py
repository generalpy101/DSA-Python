'''
Problem : Check whether given parentheses string has all its parentheses closed.
We have 6 characters, (),[] and {} and a string will be created from them.
For example : ([]) , ([) etc.
Here in first string brackets are closed so our function will return True while
in second string a [ is remaining so our function will return False.

Approach : We will use stack for this problem. We will first start pushing our opening
brackets and when we encounter a closing bracket, we will match it from stack's top.
If top is matching our closing bracket then continue else return False.

Space and Time Complexity : O(n) in worst case
'''

from stack import Stack


def check_parentheses(string):
    s = Stack()
    mapping = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for i in string:
        if i in mapping:
            s.push(i)
        else:
            top = s.pop()
            if top == "underflow":
                return False
            if mapping[top] != i:
                return False
    if not s.is_empty():
        return False
    return True


if __name__ == "__main__":
    print(check_parentheses("([])"))  # True
    print(check_parentheses("({[]})"))  # True
    print(check_parentheses("(({[]})"))  # False
    print(check_parentheses("({[]]})"))  # False
    print(check_parentheses(")([])"))  # False
