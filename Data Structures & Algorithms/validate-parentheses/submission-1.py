class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        len_s = len(s)
        if len_s%2 != 0:
            return False
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return True
        else:
            return False
