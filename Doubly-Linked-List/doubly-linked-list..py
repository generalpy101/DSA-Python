'''
In a doubly linked list, each node has reference to both next and previous node.
'''


class Node:
    def __init__(self, val=0) -> None:
        self.data = val
        self.next = None
        self.previous = None


class DoublyLL:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def insert_head(self, val):
        temp = Node(val)
        temp.next = self.head
        if self.head is not None:
            self.head.previous = temp
        self.head = temp

    def insert(self, val) -> None:
        temp = Node(val)
        if self.head == None:
            self.insert_head(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = temp
        temp.previous = curr

    def delete_head(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next
        self.head.previous = None

    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.previous.next = None

    def reverse(self):
        if not self.head or not self.head.next:
            return

        curr = self.head
        prev = curr
        while curr:
            prev = curr
            curr.next, curr.previous = curr.previous, curr.next
            curr = curr.previous
        self.head = prev

    def __str__(self) -> str:
        res = ""
        curr = self.head
        while curr:
            res += f"{curr.data} -> "
            curr = curr.next
        res += "None"
        return res

    def __repr__(self) -> str:
        res = ""
        curr = self.head
        while curr:
            res += f"{curr.data} -> "
            curr = curr.next
        res += "None"
        return res


if __name__ == "__main__":
    dll = DoublyLL()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    dll.insert(5)
    dll.insert_head(-1)
    dll.insert_head(-2)
    dll.delete_head()
    dll.delete_end()
    dll.reverse()
    print(dll)
