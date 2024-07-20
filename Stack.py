class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def display(self):
        print("Stack elements are:", self.items)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.push(40)
stack.push(50)
stack.pop()
stack.display()