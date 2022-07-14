class Stack:
    def __init__(self):
        self.elemets = []

    def push(self, item):
        return self.elemets.append(item)

    def pop(self):
        return self.elemets.pop()

    def top(self):
        return self.elemets[-1]

    def size(self):
        return len(self.elemets)

    def is_empty(self):
        return self.size() == 0


stack = Stack()

# Huddi test yozilgani kabi biz ''Stack'' dan nima kutilayotganini yozib ketishimiz kerak.
assert stack.size() == 0
assert stack.is_empty() == True

stack.push("Alex")
assert stack.size() == 1
assert stack.is_empty() == False
assert stack.top() == "Alex"

stack.push("John")
assert stack.size() == 2
assert stack.is_empty() == False
assert stack.top() == "John"
assert stack.pop() == "John"

assert stack.size() == 1
assert stack.is_empty() == False
assert stack.top() == "Alex"

assert stack.pop() == "Alex"
assert stack.size() == 0
assert stack.is_empty() == True
