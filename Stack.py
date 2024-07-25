class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack is Full")
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")

    def is_full(self):
        return len(self.items) == self.max_size

    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print("Stack elements are:", self.items)

# Example usage
max_size = 5
stack = Stack(max_size)
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.push(40)
stack.push(50)
stack.pop()
stack.display()