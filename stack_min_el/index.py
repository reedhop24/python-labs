class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.min = 0

    def __str__(self):
        temp = self.top
        output = []
        while temp:
             output.append(str(temp))
             temp = temp.next
        output = '\n'.join(output)
        return output

    def getMin(self):
        if self.top is None:
            return 'Stack is empty'
        else:
            print(self.min)

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def __len__(self):
        self.count = 0
        temp = self.top
        while temp:
            temp = temp.next
            self.count += 1
        return self.count

    def top_of_stack(self):
        if self.top is None:
            return 'Stack is empty'
        else:
            if self.top.value < self.min:
                return self.min
            else:
                return self.top.value

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.min = value
        elif value < self.min:
            temp = (2*value)-self.min
            print(temp, 'temp')
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.min = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))

    def pop(self):
        if self.top is None:
            return 'Stack is empty'
        else:
            removed_node = self.top.value
            self.top = self.top.next
            if removed_node < self.min:
                print ("Top Most Element Removed :{} " .format(self.min)) 
            else:
                print("Top Most Element Removed: {} ".format(removed_node))


stack = Stack()  
  
stack.push(3) 
stack.push(5)  
stack.getMin()
stack.push(2) 
stack.push(1) 
stack.getMin()    
stack.pop()
stack.getMin()
stack.pop() 
stack.top_of_stack()