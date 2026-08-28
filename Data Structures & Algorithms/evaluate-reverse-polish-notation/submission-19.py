class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop()+stack.pop())
            elif t == "-":
                num = stack.pop()
                nums = stack.pop()
                stack.append(nums-num)
            elif t == "*":
                stack.append(stack.pop()*stack.pop())
            elif t == "/":
                div = stack.pop()
                divisor = stack.pop()
                stack.append(int(float(divisor)/ div))
            else:
                stack.append(int(t))
        
        return stack[0]