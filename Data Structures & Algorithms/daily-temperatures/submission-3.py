class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        n = 0
        while n <= len(temperatures)-1:
            if not stack:
                stack.append(n)
                n += 1
            else:
                if temperatures[n] > temperatures[stack[-1]]:
                    res[stack[-1]] = n - stack[-1]
                    stack.pop()
                else:
                    stack.append(n)
                    n += 1
        return res





                    

            
            

            