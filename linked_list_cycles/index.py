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
            while(pointer.next):
                pointer = pointer.next
            pointer.next = new_node

    def print_all(self):
        pointer = self.head
        while(pointer):
            print(pointer.data)
            pointer = pointer.next

    def has_cycles(self):
        pointer = self.head
        vals = set()
        while(pointer):
            if pointer.data in vals:
                return True
            vals.add(pointer.data)
            pointer = pointer.next
        return False

llist = LinkedList()
llist.head = Node(5)
llist.append(4)
llist.append(3)
llist.append(2)
llist.head.next.next.next.next = llist.head

print(llist.has_cycles())