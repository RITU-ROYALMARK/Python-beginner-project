from collections import deque

class stack:
    def __init__(self):
        self.stack = deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def show_stack(self):
        return self.stack
    def len(self):
        if len(self.stack) == 0:
            return "Zero Elements"
        else:
            return f"the len of the stack is: {len(self.stack)} "
































































































































































