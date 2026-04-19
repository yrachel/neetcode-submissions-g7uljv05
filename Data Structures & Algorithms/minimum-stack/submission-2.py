class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, val: int) -> None:
        if self.mini == None or val < self.mini:
            self.mini = val
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()

        if popped == self.mini:
            if len(self.stack) == 0:
                self.mini = None
            else:
                self.mini = min(self.stack)

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini
