'''
Stack is a linear data structure. It is like a one sided closed box where you can insert and 
remove items only from top.

            |           |
            |           |
            |           |
            |-----------|
            |     2     | <- top
            |___________|
Above picture is a stack. Here we can only insert and remove items from top.
There are 4 major operations in a stack :
    push : In push operation we put a value on top of stack.
    pop  : In pop operation we remove value from top of stack.
    peek : In peek operation we get top element of stack.
    size : In size operations, size of stack is returned.
There are 2 ways to implement stack generally, using linked list or arrays. Since Arrays in most
languages are fixed sized, linked list is preffered. In python we can use lists. Other data structures 
can also be used.

There are 2 special conditions in stack :
    Underflow : It happens when we peek or pop from empty stack.
    Overflow  : It happens when we push in a full stack. Usually doesn't happens in library implementations
    of stack as it uses dynamic allocation, linked list or something like that.
'''

import single_linked_list as _

class Stack :
    def __init__(self) -> None:
        self.ll = _.LinkedList()
        self.length = 0
    
    def is_empty(self) :
        return self.length == 0

    def push(self,val) :
        self.ll.insertHead(val)
        self.length += 1

    def pop(self) :
        if self.is_empty() :
            return "underflow"
        self.length -= 1
        return self.ll.deleteHead()
    
    def peek(self) :
        if self.is_empty() :
            return "underflow"
        return self.ll.head.data

    def size(self) :
        return self.length
    
    def __len__(self) :
        return self.length

    def __str__(self) -> str:
        res = "Top -> "
        res += self.ll.__str__()
        return res
    
    def __repr__(self) -> str:
        res = "Top -> "
        res += self.ll.__repr__()
        return res
    

if __name__ == "__main__" :
    stack = Stack()
    print(stack.peek())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack)