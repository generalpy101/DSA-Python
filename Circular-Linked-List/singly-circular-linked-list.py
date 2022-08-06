'''
In circular linked list, there is a cycle present. Let's take a singly linked list :
1 -> 2 -> 3 -> 4 -> None. In the linked list, if we connect last node with value 4 to head
again it will become a singly circular linked list.
'''


class Node:
    def __init__(self, val=0) -> None:
        self.data = val
        self.next = None


class CircularLL:
    def __init__(self, head=None) -> None:
        self.head = head
        self.length = 0

    def insertBeg(self, val):
        if not self.head:
            self.head = temp
            temp.next = temp
            self.length += 1
            return
        temp = Node(val)
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = temp
        temp.next = self.head
        self.head = temp
        self.length += 1

    def insertBegOpt(self, val):
        '''
            Insert after head then swap data.
        '''
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp
        temp.data, self.head.data = self.head.data, temp.data
        self.length += 1

    def push(self, val):
        temp = Node(val)
        if not self.head:
            self.head = temp
            temp.next = self.head
            self.length += 1
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = temp
        temp.next = self.head
        self.length += 1

    def pushOpt(self, val):
        temp = Node(val)
        if not self.head:
            self.head = temp
            temp.next = self.head
            self.length += 1
            return
        temp.next = self.head.next
        self.head.next = temp
        temp.data, self.head.data = self.head.data, temp.data
        self.head = temp
        self.length += 1

    def deleteHead(self):
        if self.head == None:
            return
        if self.head.next == self.head:
            self.head = None
            self.length -= 1
            return
        curr = self.head
        while curr.next is not self.head:
            curr = curr.next
        curr.next = self.head.next
        self.head = curr.next
        self.length -= 1

    def deleteHeadOpt(self):
        if self.head == None:
            return
        if self.head.next == self.head:
            self.head = None
            self.length -= 1
            return
        curr = self.head.next
        self.head.data, curr.data = curr.data, self.head.data
        self.head.next = curr.next
        self.length -= 1
    
    def deletePos(self,pos) :
        pos = pos % self.length
        if self.head == None :
            return
        if pos == 0 :
            self.deleteHeadOpt()
            return
        else :
            curr = self.head
            for i in range(pos - 2) :
                curr = curr.next
            curr.next = curr.next.next
            self.length -= 1

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        if self.head is None:
            return
        curr = self.head.next
        res = ""
        res += f"{self.head.data} -> "
        while curr != self.head:
            res += f"{curr.data} -> "
            curr = curr.next
        res += f"{self.head.data}"
        return res

    def __repr__(self) -> str:
        if self.head is None:
            return
        curr = self.head.next
        res = ""
        res += f"{self.head.data} -> "
        while curr != self.head:
            res += f"{curr.data} -> "
            curr = curr.next
        res += f"{self.head.data}"
        return res


if __name__ == "__main__":
    cll = CircularLL()
    cll.push(1)
    cll.push(2)
    cll.push(3)
    cll.push(4)
    cll.pushOpt(5)
    cll.insertBeg(-1)
    cll.insertBegOpt(-2)
    print(cll)  # -2->-1->1->2->3->4->5->-2
    print(len(cll))  # 7
    cll.deleteHead()
    cll.deleteHeadOpt()
    print(cll)
    cll.deletePos(3)
    print(cll)