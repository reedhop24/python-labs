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
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node

    def remove_nth(self, nth):
        incrementer = 1
        pointer = self.head

        if incrementer == nth:
            self.head = pointer.next
            pointer = None
            return

        while pointer:
            if incrementer == nth:
                break
            prev = pointer
            pointer = pointer.next
            incrementer += 1

        if pointer == None:
            return
        
        prev.next = pointer.next
        pointer = None
        

llist = LinkedList()
llist.head = Node(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.remove_nth(2)
llist.print_all()



