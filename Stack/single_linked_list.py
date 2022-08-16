'''
    Linked list is an linear data structure which stores data in non contiguous locations.
    Its idea is to remove contiguous locations like in arrays to make insert and delete faster.
    Each element in a linked list contains 2 items, its data and reference to the next node of 
    the linked list.
    Worst case for insertion and deletion at beginning and end of linked list is O(1).
    Worst case for insertion and deletion in middle is O(1) if we have an reference to previous nodes.
    Merging two linked lists is faster than arrays.
'''


class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, val=None):
        if val:
            self.head = Node(val)
            self.length = 0
        else:
            self.head = None
            self.length = 1

    # Insert operations begin
    # ================================
    def push(self, val):
        if self.head == None:
            self.head = Node(val)
            self.length += 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.length += 1

    def insertHead(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.length += 1

    def insert(self, pos, val):
        if pos > self.length:
            self.push(val)
        elif pos == 0:
            self.insertHead(val)
        else:
            curr = self.head
            # I am using 0 indexed linked list so I am using pos - 1\
            # 0 indexed means for ll 1->3->12->4->9->None if I insert at
            # pos 3 element will be inserted after 12.
            # Here indices are 0 : 1, 1 : 3, 2 : 12, 4 : 3 so pos 3 is
            # occupied by 4 before insertion of 5.
            # To make ll 1 indexed i.e 5 will be inserted after 3, use pos - 2
            for i in range(pos - 1):
                curr = curr.next
            temp = Node(val)
            temp.next = curr.next
            curr.next = temp
            self.length += 1
    # Insert operations end
    # ================================

    # Delete operations begin
    # ================================

    def deleteHead(self) -> int:
        if not self.head:
            return
        val = self.head.data
        self.head = self.head.next
        self.length -= 1
        return val

    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            return self.deleteHead()
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            val = curr.data
            curr.next = None
            self.length -= 1
            return curr.data

    # Delete operations end
    # ================================

    def reverse(self):
        '''
        Reverses linked list in place
        '''
        if self.length == 0:
            return
        curr = self.head
        prev = None
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def recursive1Helper(self, head):
        if not head:
            return head
        if not head.next:
            return head
        rest_head = self.recursive1Helper(head.next)
        rest_tail = head.next
        rest_tail.next = head
        head.next = None
        return rest_head

    def reverseRecursive1(self, head=None):
        self.head = self.recursive1Helper(head)

    def reverse2Helper(self, curr, prev=None):
        if curr == None:
            return prev

        nxt = curr.next
        curr.next = prev
        return self.reverse2Helper(nxt, curr)

    def reverseRecursive2(self, head):
        self.head = self.reverse2Helper(head)

    def search(self, val):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == val:
                return pos
            pos += 1
            curr = curr.next
        return -1

    def print(self) -> None:
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print("None")

    def __repr__(self) -> str:
        res = ""
        curr = self.head
        for i in range(self.length):
            res += f"{curr.data} -> "
            curr = curr.next
        res += "None"
        return res

    def __str__(self) -> str:
        res = ""
        curr = self.head
        for i in range(self.length - 1):
            res += f"{curr.data} -> "
            curr = curr.next
        res += "None"
        return res


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(3)
    ll.push(12)
    ll.push(4)
    ll.push(9)
    print(f"{4} found at {ll.search(4)}")
    print(f"{24} found at {ll.search(24)}")
    ll.insertHead(1)
    ll.print()
    ll.insert(3, 5)
    ll.insert(0, 6)
    ll.insert(44, 7)
    ll.deleteHead()
    ll.pop()
    ll.print()
    ll.reverse()
    print(ll)  # Testing native print functionality
    ll.reverseRecursive1(ll.head)
    print(ll)  # List will be back to normal
    ll.reverseRecursive2(ll.head)
    print(ll)  # List will be reversed again
