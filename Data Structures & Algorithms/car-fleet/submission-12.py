class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(reverse=True)
        stack = []
        for p, s in ps:
            ttt = (target-p)/s
            stack.append(ttt)
            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)