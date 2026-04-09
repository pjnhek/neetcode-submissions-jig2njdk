class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": lambda x, y: x+y, "-": lambda x,y: x-y,
                "*": lambda x,y: x*y, "/": lambda x,y: int(x/y)}
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[i](b, a))
        return stack[-1]