class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack empty OR this value is <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]




stack = []
min_stack = []

def push(val):
    stack.append(val)
    if not min_stack or val <= min_stack[-1]:
        min_stack.append(val)

def pop():
    val = stack.pop()
    if val == min_stack[-1]:
        min_stack.pop()

def top():
    return stack[-1]

def get_min():
    return min_stack[-1]
