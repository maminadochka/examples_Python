class OurStack:

    def __init__(self):
        self.stack = []
        self.max_collection = []

    def pop(self):
        value = self.stack.pop()
        if self.max_collection[-1] == value:
            del self.max_collection[-1]
        return value

    def push(self, value):
        if not self.max_collection:
            self.max_collection.append(value)
        if self.max_collection[-1] <= value:
            self.max_collection.append(value)
        self.stack.append(value)

    def max(self):
        return self.max_collection[-1]

    def __str__(self):
        return ''.join(str(self.stack))


s = OurStack()

s.push(3)
s.push(5)
s.push(4)
s.pop()
s.push(2)
s.push(10)
s.pop()


print(s)
print(s.max())
