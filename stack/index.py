class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, val):
        self.stack.append(val)

    def get_value(self):
        return self.stack.pop(len(self.stack)-1)


new_stack = Stack()
new_stack.insert(4)
new_stack.insert(5)
new_stack.insert(6)
new_stack.insert(7)
new_stack.insert(8)
print(new_stack.get_value())