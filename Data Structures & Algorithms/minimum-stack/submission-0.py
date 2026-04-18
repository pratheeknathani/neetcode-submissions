class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        temp = self.stack[-1]
        self.stack = self.stack[:-1]
        return temp
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minVal = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < minVal:
                minVal = self.stack[i]
        return minVal
        
