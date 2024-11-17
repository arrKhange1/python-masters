class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Первый элемент:", queue.peek())  
print("Удаляем элемент:", queue.dequeue()) 
print("Новый первый элемент:", queue.peek())
print("Очередь пуста?", queue.is_empty())
print("Размер очереди:", queue.size()) 

    