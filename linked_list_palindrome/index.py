import copy

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

def print_all(vals):
        pointer = vals.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

def list_reverse(to_reverse):
        new_llist = LinkedList()
        p1 = None
        p2 = to_reverse.head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        to_reverse.head = p1
        new_llist.head = p1
        return new_llist

def is_palindrome(list1, list2):
    p1 = list1.head
    p2 = list2.head
    while p1 or p2:
        if p1 and p2 is None or p2 and p1 is None:
            return False
        if p1.data != p2.data:
            return False
        else:
            p1 = p1.next
            p2 = p2.next
    return True

llist = LinkedList()
llist.append('K')
llist.append('A')
llist.append('Y')
llist.append('A')
llist.append('K')


llist_r = copy.deepcopy(llist)
reversed_list = list_reverse(llist_r)
print_all(reversed_list)
print_all(llist)

print(is_palindrome(llist, reversed_list))
