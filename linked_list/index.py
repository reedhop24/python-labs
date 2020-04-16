class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_all(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, prev_node, data):
        pointer = self.head
        while pointer:
            if pointer.data == prev_node:
                new_node = Node(data)
                new_node.next = pointer.next
                pointer.next = new_node
            pointer = pointer.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node

    def remove(self, key):
        temp = self.head

        if temp:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None 


llist = LinkedList()
llist.head = Node(5)
second = Node(6)
third = Node(8)

llist.head.next = second
second.next = third
llist.push(9)
llist.insert_after(6, 11)
llist.append(69)
llist.remove(6)
llist.print_all()