class MinStack:

    def __init__(self):
        self.length = -1
        self.min_value = float('inf')
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        

        if self.length == -1:
            smallest = val            
        else:
            smallest = val if val < self.min_stack[self.length] else self.min_stack[self.length]

        self.stack.append(val)
        self.min_value = smallest
        self.min_stack.append(smallest)
        self.length += 1
        

    def pop(self) -> None:
        self.min_stack.pop(self.length)
        self.stack.pop(self.length)
        self.length -= 1

        
        

    def top(self) -> int:
        return self.stack[self.length]

    def getMin(self) -> int:
        return self.min_stack[self.length]
        
