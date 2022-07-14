class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        return self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]

    # size() - funksiya o`niga __len__ metodi ishlatildi.
    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return f"Stack({self.elements}) Size: {len(self)}"

    def __repr__(self):
        return F"Stack{self.elements}"

    def is_empty(self):
        return len(self) == 0


stack = Stack()
stack.push('Alisher')
stack.push('Sherzod')
stack.push('Sherali')
stack.pop()

print(len(stack))  # Bu yerda len() funskiyasini ishlatish uchun class ichida __len__(self) ni ham ishlatish kerak.
print(stack)  # __str__ dunder method ishlaydi
print([stack])  # __repr__ dunder method ishlaydi
