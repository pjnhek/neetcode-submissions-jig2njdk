class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                curr = stack.pop()
                res[curr[0]] = i - curr[0]
            stack.append([i, t])
        return res