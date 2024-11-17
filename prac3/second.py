class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Верхний элемент:", stack.peek())
print("Удаляем элемент:", stack.pop()) 
print("Новый верхний элемент:", stack.peek()) 
print("Стек пуст?", stack.is_empty())  
print("Размер стека:", stack.size())