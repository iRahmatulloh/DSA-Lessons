class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        # BU Pure code -- stack uzunligi 0ga teng bo'lsa True qaytaradi
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1]
    

# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.push(4)
# print(my_stack.stack)
# my_stack.pop()
# print(my_stack.stack)

# my_stack.peek()
# print(my_stack.stack)
# print(my_stack.is_empty())

def reverse_text(text):
    my_stack = Stack()
    res = ""
    for i in text:
        my_stack.push(i)

    while my_stack.stack:
        res += my_stack.pop()

    return res


print(reverse_text('salom'))
