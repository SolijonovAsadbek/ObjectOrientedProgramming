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

print('Actual: ', stack.size(), 'Expected: 0')
print('Actual: ', stack.is_empty(), 'Expected: True')

stack.push('Alex')
print('Actual: ', stack.size(), 'Expected: 1')
print('Actual: ', stack.is_empty(), 'Expected: Fale')
print('Actual: ', stack.top(), 'Expected: Alex')

stack.push('John')
print('Actual: ', stack.size(), 'Expected: 2')
print('Actual: ', stack.is_empty(), 'Expected: Fale')
print('Actual: ', stack.top(), 'Expected: John')
print('Actual: ', stack.pop(), 'Expected: John')

print('Actual: ', stack.size(), 'Expected: 1')
print('Actual: ', stack.is_empty(), 'Expected: Fale')
print('Actual: ', stack.top(), 'Expected: Alex')

print('Actual: ', stack.pop(), 'Expected: Alex')
print('Actual: ', stack.size(), 'Expected: 0')
print('Actual: ', stack.is_empty(), 'Expected: True')