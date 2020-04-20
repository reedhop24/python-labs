class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node

    def print_all(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def reverse(self):
        p1 = None
        p2 = self.head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        self.head = p1

llist = LinkedList()
llist.append(5)
llist.append(4)
llist.append(3)
llist.append(2)
llist.append(1)
llist.print_all()
llist.reverse()
llist.print_all()
