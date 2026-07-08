class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dic = {")": "(", "}": "{", "]": "["}
        stack = []
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] in bracket_dic.values() or not stack:
                stack.append(s[l])
            else:
                if bracket_dic[s[l]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            l += 1
        if not stack:
            return True
        else:
            return False