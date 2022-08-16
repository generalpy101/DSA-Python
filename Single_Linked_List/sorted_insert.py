'''
Problem : Insert a given element in a sorted linked list such that the linked list remains sorted.
Eg : ll=1->4->5->10 and we need to insert 7 in it. After our operations, final linked list must be
     ll=1->4->5->7->10
'''

from single_linked_list import LinkedList

def insert_sorted(linkedList,element) :
    if linkedList.length == 0 :
        linkedList.insertHead(element)
    else :
        pos = 0
        curr = linkedList.head
        while curr and curr.data < element:
           curr = curr.next
           pos += 1
        linkedList.insert(pos,element)

if __name__ == '__main__' :
    ll = LinkedList(1)
    ll.push(4)
    ll.push(5)
    ll.push(10)
    print("Inserting 7,0 and 10")
    print("Before insertion : ",end="")
    ll.print()
    insert_sorted(ll,7)
    assert ll.search(7) == 3
    insert_sorted(ll,0)
    assert ll.search(0) == 0
    insert_sorted(ll,12)
    assert ll.search(12) == ll.length
    print("After insertion : ",end = "")
    ll.print()
    print("Inserting in empty list")
    print("Inserting 10")
    ll1 = LinkedList()
    insert_sorted(ll1,10)
    assert ll1.head.data == 10
    print("After insertion : ")
    ll1.print()
    print("Insertion successful in all cases")