class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
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

    def find_beginnig(self):
        hash_set = set()
        pointer = self.head
        while pointer:
            if pointer.data in hash_set:
                return 'Loop is: ' + str(pointer.data)
            hash_set.add(pointer.data)
            pointer = pointer.next
        return -1

llist = LinkedList()
llist.insert(5)
llist.insert(4)
llist.insert(3)
llist.insert(2)
llist.insert(1)
llist.insert(4)
print(llist.find_beginnig())