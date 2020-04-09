class Queue:
    def __init__(self):
        self.queue = []
    
    def insert(self, val):
        self.queue.append(val)

    def get_value(self):
        return self.queue.pop(0)

new_queue = Queue()
new_queue.insert(30)
new_queue.insert(40)
new_queue.insert(50)
new_queue.insert(60)
new_queue.insert(70)

print(new_queue.get_value())
print(new_queue.get_value())
print(new_queue.get_value())