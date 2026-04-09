class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minStk) == 0 or self.minStk[-1] >= val:
            self.minStk.append(val)
        

    def pop(self) -> None:
        if self.minStk[-1] == self.stk[-1]:
            self.minStk.pop()
        self.stk.pop()

        
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minStk[-1]
        
