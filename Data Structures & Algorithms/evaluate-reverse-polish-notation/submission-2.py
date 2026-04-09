class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = []
        ops = {"+": lambda L: L[0]+L[1], "-": lambda L: L[0]-L[1], 
        "*": lambda L: L[0]*L[1], "/": lambda L: int(L[0]/L[1])}
        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError:
                n = 2
                while n > 0:
                    n -= 1
                    print(stack)
                    res.append(stack.pop())
                res[0], res[1] = res[1], res[0]
                stack.append(ops[i](res))
                res = []
        return stack[-1]
